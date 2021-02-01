#!/usr/bin/env python3
# thamos
# Copyright(C) 2018, 2019, 2020 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""CLI and library configuration."""

import logging
import os
import typing
from urllib.parse import urljoin
from jsonschema import validate

import click
import requests
import yaml

from thoth.common import normalize_os_version
from thoth.common import map_os_name

from .utils import workdir
from .discover import discover_cpu
from .discover import discover_cuda_version
from .discover import discover_distribution
from .discover import discover_python_version
from .discover import discover_platform
from .discover import discover_base_image
from .exceptions import NoApiSupported
from .exceptions import NoRuntimeEnvironmentError
from .exceptions import ConfigurationError
from .exceptions import NoProjectDirError
from .exceptions import ServiceUnavailable

_LOGGER = logging.getLogger(__name__)
_THAMOS_DISABLE_TLS_WARNING = bool(int(os.getenv("THAMOS_DISABLE_TLS_WARNING", 0)))
_API_CONNECTION_TIMEOUT = int(os.getenv("THAMOS_API_CONNECTION_TIMEOUT", 5))

# The schema is enforcing all the options. This will make sure the right version of Thamos is
# installed and no configuration options are silently ignored.
_CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "host": {"type": "string", "format": "hostname"},
        "tls_verify": {"type": "boolean"},
        "requirements_format": {
            "type": "string",
            "enum": ["pipenv", "pip", "pip-tools"],
        },
        "runtime_environments": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "cuda_version": {"type": ["string", "null"]},
                    "openblas_version": {"type": ["string", "null"]},
                    "openmpi_version": {"type": ["string", "null"]},
                    "cudnn_version": {"type": ["string", "null"]},
                    "mkl_version": {"type": ["string", "null"]},
                    "base_image": {"type": ["string", "null"]},
                    "hardware": {
                        "type": "object",
                        "properties": {
                            "cpu_family": {"type": "integer"},
                            "cpu_model": {"type": "integer"},
                            "gpu_model": {"type": ["string", "null"]},
                        },
                        "required": [],
                        "additionalProperties": False,
                    },
                    "name": {"type": "string", "pattern": r"^[a-zA-Z0-9:_-]+$"},
                    "operating_system": {
                        "type": "object",
                        "properties": {
                            "name": {"type": ["string", "null"]},
                            "version": {"type": ["string", "null"]},
                        },
                        "required": ["name", "version"],
                        "additionalProperties": False,
                    },
                    "platform": {"type": ["string", "null"]},
                    "python_version": {
                        "type": "string",
                        "pattern": r"^[0-9]+\.[0-9]+$",
                    },
                    "recommendation_type": {
                        "type": "string",
                        "enum": [
                            "latest",
                            "stable",
                            "performance",
                            "security",
                            "testing",
                        ],
                    },
                },
                "additionalProperties": False,
                "required": ["name"],
            },
        },
        "managers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                },
                "additionalProperties": True,
                "required": ["name"],
            },
        },
    },
    "required": ["host", "runtime_environments"],
}


class _Configuration:
    """Handling of Thoth's configuration."""

    DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
    DEFAULT_THOTH_CONFIG = os.path.join(DATA_DIR, "defaultThoth.yaml")
    CONFIG_NAME = ".thoth.yaml"
    REQUIREMENTS_FORMATS = frozenset(("pip", "pip-tools", "pip-compile", "pipenv"))
    _DEFAULT_REQUIREMENTS_FORMAT = "pipenv"
    _TLS_WARNING_LOGGED = False

    def __init__(self):
        """Construct configuration instance."""
        self._configuration = None
        self._index_aicoe = None
        # Thoth instance to be used when explicitly said by user - the one stated in
        # configuration file will be omitted.
        self.explicit_host = None
        self.tls_verify = None
        self._api_url = None

    @property
    def api_url(self):
        """Get URL to Thoth's API."""
        if not self._api_url:
            self._api_url = self.api_discovery(self.content["host"])

        return self._api_url

    @property
    def content(self):
        """Access configuration."""
        if not self._configuration:
            self.load_config()

        return self._configuration

    @property
    def requirements_format(self) -> str:
        """Check requirements_format in configuration."""
        requirements_format = self.content.get("requirements_format") or "pipenv"

        if not isinstance(requirements_format, str):
            raise ConfigurationError(
                "The data type for requirements_format should be str"
            )

        if requirements_format not in ("pip", "pip-tools", "pipenv"):
            raise ValueError(
                f"Unknown configuration option for requirements format: {requirements_format!r}"
            )

        return requirements_format

    def get_thoth_version(self) -> str:
        """Get version of Thoth backend."""
        _LOGGER.debug(
            "Contacting Thoth at %r to receive version information", self.api_url
        )
        response = requests.head(
            self.api_url, verify=self.tls_verify, timeout=_API_CONNECTION_TIMEOUT
        )
        response.raise_for_status()
        return response.headers.get("X-Thoth-Version", "Not Available")

    def config_file_exists(self) -> bool:
        """Check if configuration file exists."""
        try:
            with workdir(self.CONFIG_NAME):
                return True
        except NoProjectDirError:
            return False

    def load_config_from_string(self, config_str: str) -> None:
        """Load configuration from a string."""
        if int(os.getenv("THAMOS_CONFIG_EXPAND_ENV", 0)):
            _LOGGER.info("Expanding configuration file based on environment variables")
            config_str = config_str.format(**os.environ)

        self._configuration = yaml.safe_load(config_str)

    def load_config_from_file(self, config_path: str) -> None:
        """Load configuration from a file."""
        with open(config_path, "r") as config_file:
            self._configuration = config_file.read()

            if int(os.getenv("THAMOS_CONFIG_EXPAND_ENV", 0)):
                _LOGGER.info(
                    "Expanding configuration file based on environment variables"
                )
                self._configuration = self._configuration.format(**os.environ)

            self._configuration = yaml.safe_load(self._configuration)

    def load_config(self, force: bool = False) -> None:
        """Load configuration from a file."""
        if not self._configuration and not force:
            with workdir(config.CONFIG_NAME):
                self.load_config_from_file(config.CONFIG_NAME)

    def create_default_config(
        self, template: str = None, nowrite: bool = False
    ) -> typing.Optional[dict]:
        """Place default configuration into the current directory."""
        if not os.path.isdir(".git"):
            _LOGGER.warning("Configuration file is not created in the root of git repo")

        template = template or self.DEFAULT_THOTH_CONFIG
        _LOGGER.debug("Reading configuration from %r", template)
        with open(template, "r") as default_config_file:
            default_config = default_config_file.read()

        _LOGGER.info("Discovering host runtime environment")

        cpu_info = discover_cpu()
        cuda_version = discover_cuda_version()
        # Add quotes for textual representation in the config file.
        cuda_version = f"'{cuda_version}'" if cuda_version is not None else "null"
        os_name, os_version = discover_distribution()
        os_name = map_os_name(os_name)
        os_version = normalize_os_version(os_name, os_version)
        python_version = discover_python_version()
        platform = discover_platform()
        base_image = discover_base_image()
        base_image = base_image if base_image is not None else "null"

        requirements_format = os.getenv(
            "THAMOS_REQUIREMENTS_FORMAT", self._DEFAULT_REQUIREMENTS_FORMAT
        )
        if requirements_format not in self.REQUIREMENTS_FORMATS:
            # This avoids possibly dangerous environment variable expansion.
            _LOGGER.warning(
                "Unknown requirements format specified, forcing %r: %r",
                self._DEFAULT_REQUIREMENTS_FORMAT,
                requirements_format,
            )
            requirements_format = self._DEFAULT_REQUIREMENTS_FORMAT

        expand_env = bool(int(os.getenv("THAMOS_CONFIG_EXPAND_ENV", 0)))
        default_config = default_config.format(
            cuda_version=cuda_version,
            os_name=os_name,
            os_version=os_version,
            python_version=python_version,
            platform=platform,
            requirements_format=requirements_format,
            base_image=base_image,
            **cpu_info,
            **(dict(os.environ) if expand_env else {}),
        )

        if not nowrite:
            _LOGGER.debug(
                "Writing configuration file to %r",
                os.path.join(os.getcwd(), self.CONFIG_NAME),
            )

            with open(self.CONFIG_NAME, "w") as config_file:
                config_file.write(default_config)
            return None
        else:
            return yaml.safe_load(default_config)

    @staticmethod
    def open_config_file():
        """Open Thoth's configuration file."""
        with workdir(config.CONFIG_NAME):
            _LOGGER.debug("Opening configuration file %r", config.CONFIG_NAME)
            click.edit(filename=config.CONFIG_NAME)

    def list_runtime_environments(self):
        """List available runtime environments."""
        return self.content.get("runtime_environments", [])

    def get_runtime_environment(self, name: str = None) -> typing.Optional[dict]:
        """Get runtime environment, retrieve the first runtime environment (the default one) if no name is provided."""
        content = self.content
        if "runtime_environments" not in content:
            raise NoRuntimeEnvironmentError(
                "No runtime environment configuration stated in the configuration file "
                "under 'runtime_environments' configuration entry"
            )

        if not isinstance(content["runtime_environments"], list):
            raise ConfigurationError(
                "The data type for requirements_format should be list"
            )

        to_return = None
        seen_names = set()
        for idx, runtime_environment in enumerate(content["runtime_environments"]):
            if not isinstance(runtime_environment, dict):
                raise ConfigurationError(
                    "Unknown runtime configuration entry, runtime configuration should be "
                    "a dictionary; got: %r",
                    runtime_environment,
                )

            # We explicitly iterate over all entries to perform the following sanity checks.
            current_name = runtime_environment.get("name")
            if current_name is not None and current_name in seen_names:
                raise ConfigurationError(
                    "Multiple configuration options with name %r found in the configuration file",
                    current_name,
                )

            if idx > 0 and current_name is None:
                raise ConfigurationError(
                    "Assign explicitly name for each configuration entry if there are multiple "
                    "runtime configuration options to distinguish between them"
                )

            if current_name is not None:
                seen_names.add(current_name)

            if name is None and idx == 0:
                # Return the first one by default.
                to_return = runtime_environment
            elif current_name == name:
                # Return by name.
                to_return = runtime_environment

        if to_return is None and len(content["runtime_environments"]) > 0:
            if name is not None:
                raise NoRuntimeEnvironmentError(
                    f"No runtime environment with name {name!r} was found in the configuration file; "
                    f"configured runtime environment names: {','.join(seen_names)}"
                )

            raise NoRuntimeEnvironmentError(
                "No runtime environment configuration was found"
            )

        return to_return

    def api_discovery(self, host: str) -> str:
        """Discover API versions available, return the most recent one supported by client and server."""
        api_url = urljoin("https://" + host, "api/v1")
        self.tls_verify = (
            self.tls_verify
            if self.tls_verify is not None
            else self.content.get("tls_verify", True)
        )

        if (
            not self.tls_verify
            and not _THAMOS_DISABLE_TLS_WARNING
            and not self._TLS_WARNING_LOGGED
        ):
            self._TLS_WARNING_LOGGED = True
            _LOGGER.warning(
                "TLS verification turned off, its highly recommended to use a secured connection, "
                "see configuration file for configuration options"
            )

        response = requests.get(
            api_url, verify=self.tls_verify, headers={"Accept": "application/json"}
        )

        try:
            response.raise_for_status()
        except Exception as exc:
            if response.status_code == 503:
                _LOGGER.error("Thoth service at %r is unavailable (HTTP 503)", api_url)
                raise ServiceUnavailable(str(exc))

            raise NoApiSupported(
                "Server does not support API v1 required by Thamos client"
            ) from exc

        self._api_url = api_url
        return self._api_url

    def check_runtime_environment(
        self, runtime_environment_name: str
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """Check the given runtime environment entry."""
        runtime_environment = self.get_runtime_environment(runtime_environment_name)

        result = []

        # CUDA
        cuda_version = discover_cuda_version()
        if runtime_environment.get("cuda_version") != cuda_version:
            if (
                cuda_version is None
                or isinstance(cuda_version, str)
                and isinstance(runtime_environment.get("cuda_version"), str)
            ):
                message_type = "ERROR"
            else:
                message_type = "WARNING"

            result.append(
                {
                    "type": message_type,
                    "runtime_environment": runtime_environment_name,
                    "message": f"CUDA version declared in the configuration file "
                    f"({runtime_environment['cuda_version']!r}) does not match the one detected ({cuda_version!r})",
                }
            )

        # Operating system
        if runtime_environment.get("operating_system"):
            conf_os_name = map_os_name(
                runtime_environment["operating_system"].get("name")
            )
            conf_os_version = normalize_os_version(
                conf_os_name, runtime_environment["operating_system"].get("version")
            )

            if conf_os_name == "ubi":
                result.append(
                    {
                        "type": "INFO",
                        "runtime_environment": runtime_environment_name,
                        "message": "UBI container images are ABI compatible with RHEL container images",
                    }
                )
                conf_os_name = "rhel"

            os_name, os_version = discover_distribution()
            os_name = map_os_name(os_name)
            os_version = normalize_os_version(os_name, os_version)
            if conf_os_name != os_name:
                result.append(
                    {
                        "type": "ERROR",
                        "runtime_environment": runtime_environment_name,
                        "message": f"Operating system name stated in the configuration file ({conf_os_name!r}) "
                        f"does not match the one detected ({os_name!r})",
                    }
                )
            elif conf_os_version != os_version:
                result.append(
                    {
                        "type": "ERROR",
                        "runtime_environment": runtime_environment_name,
                        "message": f"Operating system version stated in the configuration file ({conf_os_version!r}) "
                        f"does not match the one detected ({os_version!r})",
                    }
                )

        # Python version
        python_version = discover_python_version()
        conf_python_version = runtime_environment.get("python_version")
        if python_version != conf_python_version:
            result.append(
                {
                    "type": "ERROR",
                    "runtime_environment": runtime_environment_name,
                    "message": f"Python version detected ({python_version!r}) does not match the one stated in the "
                    f"configuration file ({conf_python_version!r})",
                }
            )

        # Check hardware
        conf_cpu_family = runtime_environment.get("hardware", {}).get("cpu_family")
        conf_cpu_model = runtime_environment.get("hardware", {}).get("cpu_model")

        cpu_info = discover_cpu()
        if cpu_info.get("cpu_family") != conf_cpu_family:
            result.append(
                {
                    "type": "ERROR" if conf_cpu_family is not None else "WARNING",
                    "runtime_environment": runtime_environment_name,
                    "message": f"CPU model stated in the configuration file ({conf_cpu_family}) does not match the "
                    f"one detected ({cpu_info.get('cpu_family')})",
                }
            )

        if cpu_info.get("cpu_model") != conf_cpu_model:
            result.append(
                {
                    "type": "ERROR" if conf_cpu_model is not None else "WARNING",
                    "runtime_environment": runtime_environment_name,
                    "message": f"CPU model stated in the configuration file ({conf_cpu_model}) does not match the "
                    f"one detected ({cpu_info.get('cpu_model')})",
                }
            )

        return result

    def check(
        self, runtime_environment_name: typing.Optional[str] = None
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """Check the configuration file and produce a report."""
        result = []

        self.check_schema()

        # warn on multiple runtime environments when no overlay is used
        if (
            len(self.content["runtime_environments"]) > 1
            and self.content.get("overlays_dir") is None
        ):
            result.append(
                {
                    "message": "Multiple runtime environments defined but no overlays directory configured",
                    "type": "WARNING",
                }
            )

        if runtime_environment_name is not None:
            result.extend(self.check_runtime_environment(runtime_environment_name))
        else:
            for entry in self.content.get("runtime_environments") or []:
                result.extend(self.check_runtime_environment(entry["name"]))

        return result

    def check_schema(self) -> None:
        """Check the configuration file schema."""
        try:
            validate(instance=self.content, schema=_CONFIG_SCHEMA)
        except Exception:
            _LOGGER.error(
                "Schema validation failed: please make sure you run Thamos which supports the supplied "
                "configuration file"
            )
            raise

    def get_overlays_directory(
        self, runtime_environment_name: typing.Optional[str] = None
    ) -> str:
        """Get path to an overlays directory."""
        runtime_environment_config = self.get_runtime_environment(
            runtime_environment_name
        )
        overlays_dir = self.content.get("overlays_dir")

        with workdir(self.CONFIG_NAME):
            # No overlays directory configured.
            if overlays_dir is None:
                return os.getcwd()

            return os.path.join(overlays_dir, runtime_environment_config["name"])


config = _Configuration()
