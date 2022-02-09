#!/usr/bin/env python3
# thamos
# Copyright(C) 2018 - 2021 Fridolin Pokorny
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

"""Implementation discovery methods to detect the current environment and its configuration."""

import os
import sys
import logging
import typing
import sysconfig

from typing import Dict, Union

from thoth.common import map_os_name
from thoth.common import normalize_os_version

import distro
import click
from thoth.analyzer import run_command

_LOGGER = logging.getLogger(__name__)
_PROC_CPU_INFO = "/proc/cpuinfo"


def discover_cuda_version(interactive: bool = False) -> typing.Optional[str]:
    """Check for CUDA version, if no CUDA is installed, return None."""
    if bool(int(os.getenv("THAMOS_DISABLE_CUDA", 0))):
        _LOGGER.debug(
            "Disabling CUDA based on THAMOS_DISABLE_CUDA environment variable that is set to %r",
            os.environ["THAMOS_DISABLE_CUDA"],
        )
        return None

    result = run_command("nvcc --version", raise_on_error=False)
    if result.return_code != 0:
        _LOGGER.debug("No CUDA version detected")
        _LOGGER.debug(
            "Unable to detect CUDA version - nvcc returned non-zero version: %s",
            result.to_dict(),
        )
        return None

    lines = result.stdout.splitlines()
    version_info = lines[-1].split(",")
    if len(version_info) != 3:
        _LOGGER.debug(
            "Unable to detect CUDA version from nvcc output: %r", result.stdout
        )
        return None

    cuda_version = version_info[1].strip()[len("release ") :]

    if interactive:
        cuda_version = click.prompt("Please select CUDA version", default=cuda_version)

    _LOGGER.debug("Detected CUDA version: %r", cuda_version)
    return cuda_version


def discover_distribution() -> tuple:
    """Get distribution identifier and distribution version."""
    distribution, version, *_ = distro.linux_distribution(full_distribution_name=False)
    _LOGGER.debug("Detected running %r in version %r", distribution, version)
    os_name = map_os_name(distribution)
    return os_name, normalize_os_version(os_name, version)


def discover_python_version() -> str:
    """Discover Python version in which we run in."""
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    _LOGGER.debug("Detected running Python %r", python_version)
    return python_version


def discover_cpu() -> Dict[str, Union[str, int, None]]:
    """Discover CPU model, model name and family."""
    result = {
        "cpu_family": None,
        "cpu_model": None,
        "cpu_model_name": None,
    }  # type: Dict[str, Union[str, int, None]]

    try:
        with open(_PROC_CPU_INFO, "r") as cpu_info_file:
            content = cpu_info_file.read().splitlines()

        for line in content:
            if line.startswith("model name") and result["cpu_model_name"] is None:
                try:
                    result["cpu_model_name"] = line.split(":")[1].strip()
                except Exception as exc:
                    _LOGGER.warning(
                        "Failed to obtain CPU model name from %s: %s",
                        str(exc),
                        _PROC_CPU_INFO,
                    )
            elif line.startswith("model\t") and result["cpu_model"] is None:
                try:
                    result["cpu_model"] = int(line.split(":")[1])
                except Exception as exc:
                    _LOGGER.warning(
                        "Failed to obtain CPU model from %s: %s",
                        str(exc),
                        _PROC_CPU_INFO,
                    )
            elif line.startswith("cpu family") and result["cpu_family"] is None:
                try:
                    result["cpu_family"] = int(line.split(":")[1])
                except Exception as exc:
                    _LOGGER.warning(
                        "Failed to obtain CPU family from %s: %s",
                        str(exc),
                        _PROC_CPU_INFO,
                    )

    except Exception as exc:
        _LOGGER.exception("Failed to obtain CPU specific information: %s", str(exc))

    if result["cpu_model_name"] is None:
        # Assign a text representation - unknown for config file.
        result["cpu_model_name"] = "Unknown"

    _LOGGER.debug(
        "Detected CPU: %s", ", ".join((f"{k}: {v}" for k, v in result.items()))
    )
    return result


def discover_platform() -> str:
    """Discover platform used."""
    platform = sysconfig.get_platform()
    _LOGGER.debug("Detected running platform %r", platform)
    return platform


def discover_base_image() -> typing.Optional[str]:
    """Discover base image and its version."""
    # IMAGE_NAME and IMAGE_TAG injected by AICoE-CI take precedence over Thoth s2i.
    base_image_name = os.getenv("IMAGE_NAME", os.getenv("THOTH_S2I_NAME"))
    base_image_version = os.getenv("IMAGE_TAG")
    if base_image_version is None:
        base_image_version = os.getenv("THOTH_S2I_VERSION")
        # Add `v' to the version information for Thoth specific environment variable.
        base_image_version = f"v{base_image_version}" if base_image_version else None

    if base_image_name and base_image_version:
        base_image = f"{base_image_name}:{base_image_version}"
        _LOGGER.debug("Detected base image %r", base_image)
        return base_image
    elif base_image_name:
        _LOGGER.warning(
            "Discovered running inside %r but no base image version provided",
            base_image_name,
        )
    elif base_image_version:
        _LOGGER.warning(
            "Discovered running inside a base image in version %r but no base image name provided",
            base_image_version,
        )

    return None


def discover_all() -> typing.Dict[str, typing.Any]:
    """Discover all the entries used in Thoth's configuration file."""
    # XXX: missing autodiscovery for OpenBLAS, OpenMPI, cuDNN, MKL, hardware.gpu_model
    result = {
        "cuda_version": discover_cuda_version(),
        "python_version": discover_python_version(),
        "platform": discover_platform(),
        "base_image": discover_base_image(),
        "hardware": discover_cpu(),
    }

    os_name, os_version = discover_distribution()
    result["operating_system"] = {
        "name": os_name,
        "version": os_version,
    }

    return result
