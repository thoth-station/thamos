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

import click
import requests
import yaml

from .utils import workdir
from .discover import discover_cpu
from .discover import discover_cuda_version
from .discover import discover_distribution
from .discover import discover_python_version
from .discover import discover_platform
from .exceptions import NoApiSupported
from .exceptions import InternalError
from .exceptions import NoRuntimeEnvironmentError
from .exceptions import ConfigurationError
from .exceptions import NoProjectDirError
from .exceptions import ServiceUnavailable
from .exceptions import NoRequirementsFormatError
from urllib.parse import urljoin

_LOGGER = logging.getLogger(__name__)
_THAMOS_DISABLE_TLS_WARNING = bool(int(os.getenv("THAMOS_DISABLE_TLS_WARNING", 0)))


class _Configuration:
    """Handling of Thoth's configuration."""

    DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
    DEFAULT_THOTH_CONFIG = os.path.join(DATA_DIR, "defaultThoth.yaml")
    CONFIG_NAME = ".thoth.yaml"
    REQUIREMENTS_FORMATS = frozenset(("pip", "pip-tools", "pip-compile", "pipenv"))
    _DEFAULT_REQUIREMENTS_FORMAT = "pipenv"

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
        requirements_format = self.content.get("requirements_format")
        if not requirements_format:
            raise NoRequirementsFormatError(
                "No requirements format configuration stated in the configuration file "
                "under 'requirements_format' configuration entry"
            )

        if not isinstance(requirements_format, str):
            raise ConfigurationError("The data type for requirements_format should be str")

        if requirements_format not in ("pip", "pip-tools", "pipenv"):
            raise ValueError(f"Unknown configuration option for requirements format: {requirements_format!r}")

        return requirements_format

    def get_thoth_version(self) -> str:
        """Get version of Thoth backend."""
        _LOGGER.debug("Contacting Thoth at %r to receive version information", self.api_url)
        response = requests.head(self.api_url, verify=self.tls_verify)
        response.raise_for_status()
        return response.headers.get("X-Thoth-Version", "Not Available")

    def config_file_exists(self) -> bool:
        """Check if configuration file exists."""
        try:
            with workdir(self.CONFIG_NAME):
                return True
        except NoProjectDirError:
            return False

    def load_config(self):
        """Load configuration file."""
        with workdir(config.CONFIG_NAME):
            with open(config.CONFIG_NAME, "r") as config_file:
                self._configuration = config_file.read()

                if int(os.getenv("THAMOS_CONFIG_EXPAND_ENV", 0)):
                    _LOGGER.info("Expanding configuration file based on environment variables")
                    self._configuration = self._configuration.format(**os.environ)

                self._configuration = yaml.safe_load(self._configuration)

    def create_default_config(self, template: str = None, nowrite: bool = False) -> typing.Optional[dict]:
        """Place default configuration into the current directory."""
        if not os.path.isdir(".git"):
            _LOGGER.warning("Configuration file is not created in the root of git repo")

        template = template or self.DEFAULT_THOTH_CONFIG
        _LOGGER.debug(
            "Reading configuration from %r", template
        )
        with open(template, "r") as default_config_file:
            default_config = default_config_file.read()

        _LOGGER.info("Discovering host runtime environment")

        cpu_info = discover_cpu()
        cuda_version = discover_cuda_version()
        # Add quotes for textual representation in the config file.
        cuda_version = f"'{cuda_version}" if cuda_version is not None else 'null'
        os_name, os_version = discover_distribution()
        python_version = discover_python_version()
        platform = discover_platform()

        requirements_format = os.getenv("THAMOS_REQUIREMENTS_FORMAT", self._DEFAULT_REQUIREMENTS_FORMAT)
        if requirements_format not in self.REQUIREMENTS_FORMATS:
            # This avoids possibly dangerous environment variable expansion.
            _LOGGER.warning(
                "Unknown requirements format specified, forcing %r: %r",
                self._DEFAULT_REQUIREMENTS_FORMAT,
                requirements_format
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
            **cpu_info,
            **(os.environ if expand_env else {}),
        )

        if not nowrite:
            _LOGGER.debug(
                "Writing configuration file to %r",
                os.path.join(os.getcwd(), self.CONFIG_NAME),
            )

            with open(self.CONFIG_NAME, "w") as config_file:
                config_file.write(default_config)
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
            raise ConfigurationError("The data type for requirements_format should be list")

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

    def api_discovery(self, host: str = None) -> str:
        """Discover API versions available, return the most recent one supported by client and server."""
        api_url = urljoin("https://" + host, "/api/v1")
        self.tls_verify = (
            self.tls_verify
            if self.tls_verify is not None
            else self.content.get("tls_verify", True)
        )

        if not self.tls_verify and not _THAMOS_DISABLE_TLS_WARNING:
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

            raise NoApiSupported(
                "Server does not support API v1 required by Thamos client"
            ) from exc

        self._api_url = api_url
        return self._api_url


config = _Configuration()
