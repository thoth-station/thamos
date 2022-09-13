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

import click
import distro
import os
import sys
import logging
import sysconfig

from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

from thoth.analyzer import run_command
from thoth.common import map_os_name
from thoth.common import normalize_os_version


_LOGGER = logging.getLogger(__name__)
_PROC_CPU_INFO = "/proc/cpuinfo"


# Taken from https://github.com/rpm-software-management/yum/blob/master/rpmUtils/miscutils.py as rpmUtils was deprecated
def _split_rpm_filename(filename):
    """
    Pass in a standard style rpm fullname.

    Return a name, version, release, epoch, arch, e.g.::
        foo-1.0-1.i386.rpm returns foo, 1.0, 1, i386
        1:bar-9-123a.ia64.rpm returns bar, 9, 123a, 1, ia64
    """
    if filename[-4:] == ".rpm":
        filename = filename[:-4]

    arch_index = filename.rfind(".")
    arch = filename[arch_index + 1 :]

    rel_index = filename[:arch_index].rfind("-")
    rel = filename[rel_index + 1 : arch_index]

    ver_index = filename[:rel_index].rfind("-")
    ver = filename[ver_index + 1 : rel_index]

    epoch_index = filename.find(":")
    if epoch_index == -1:
        epoch = ""
    else:
        epoch = filename[:epoch_index]

    name = filename[epoch_index + 1 : ver_index].strip()
    return name, ver, rel, epoch, arch


def discover_cuda_version(interactive: bool = False) -> Optional[str]:
    """Check for CUDA version, if no CUDA is installed, return None."""
    thamos_disable_cuda = os.getenv("THAMOS_DISABLE_CUDA", None)
    if thamos_disable_cuda == "1":
        _LOGGER.debug(
            "Disabling CUDA based on THAMOS_DISABLE_CUDA environment variable that is set to 1",
        )
        return None

    _LOGGER.debug(
        "Enabling CUDA based on THAMOS_DISABLE_CUDA environment variable that is set to 0",
    )

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


def discover_cudnn_version() -> Optional[str]:
    """Discover CuDNN version and return None if not found."""
    result = run_command("nvcc --version", raise_on_error=False)

    if result.return_code != 0:
        _LOGGER.debug("No CUDA version detected")
        _LOGGER.debug(
            "Unable to detect CUDA version - nvcc returned non-zero version: %s",
            result.to_dict(),
        )
        return None

    for cudnn_header_path in [
        "/usr/local/cuda/include/cudnn.h",
        "/usr/include/cudnn.h",
    ]:
        cudnn_version_command = run_command(
            f"cat {cudnn_header_path} | grep CUDNN_MAJOR -A 10", raise_on_error=False
        )

        if cudnn_version_command.return_code != 0:
            _LOGGER.debug(
                f"Unable to locate cudnn.h at {cudnn_header_path.split('/')[-1]}"
            )

        else:
            cudnn_version_header = cudnn_version_command.stdout
            major_version, minor_version, patch_level = [None] * 3

            for line in cudnn_version_header.splitlines():
                if "CUDNN_MAJOR" in line and major_version is None:
                    cudnn_major_location = line.rfind("CUDNN_MAJOR") + len(
                        "CUDNN_MAJOR"
                    )
                    major_version = line[cudnn_major_location:].strip()

                if "CUDNN_MINOR" in line and minor_version is None:
                    cudnn_minor_location = line.rfind("CUDNN_MINOR") + len(
                        "CUDNN_MINOR"
                    )
                    minor_version = line[cudnn_minor_location:].strip()

                if "CUDNN_PATCHLEVEL" in line and patch_level is None:
                    cudnn_patchlevel_location = line.rfind("CUDNN_PATCHLEVEL") + len(
                        "CUDNN_PATCHLEVEL"
                    )
                    patch_level = line[cudnn_patchlevel_location:].strip()

            if major_version is None:
                _LOGGER.error(f"No cuDNN major version detected in {cudnn_header_path}")
                break

            cudnn_version = major_version
            if minor_version:
                cudnn_version += f".{minor_version}"

            if patch_level:
                cudnn_version += f".{patch_level}"

            _LOGGER.debug("Detected cuDNN version %s", cudnn_version)
            return cudnn_version

    _LOGGER.debug("No cuDNN version detected")
    return None


def discover_mkl_version() -> Optional[str]:
    """Discover MLK Python package version and return None if not found."""
    result = run_command("pip list | grep -F mkl", raise_on_error=False)

    if result.return_code != 0:
        _LOGGER.debug("No MKL Python package detected")
        return None

    return result.stdout.splitlines()[0].split(" ")[-1]


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
    }  # type: Dict[str, Any]

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

    result = {k: v or "Unknown" for k, v in result.items()}

    _LOGGER.debug(
        "Detected CPU: %s", ", ".join((f"{k}: {v}" for k, v in result.items()))
    )
    return result


def discover_platform() -> str:
    """Discover platform used."""
    platform = sysconfig.get_platform()
    _LOGGER.debug("Detected running platform %r", platform)
    return platform


def discover_base_image() -> Optional[str]:
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


def discover_rpm_package(package_name: str) -> Optional[Dict[str, str]]:
    """Check for version of a RPM package and return None if not found."""
    result = run_command(f"rpm -qa | grep {package_name}", raise_on_error=False)

    if result.return_code != 0:
        _LOGGER.debug("No %s version detected", package_name)
        _LOGGER.debug("%s not found in RPM packages", package_name)
        return None

    if result.stdout is not None:
        for line in result.stdout.splitlines():
            name, ver, rel, epoch, arch = _split_rpm_filename(line)
            if name == package_name:
                _LOGGER.debug("%s detected with version %s", package_name, ver)
                return {
                    "name": name,
                    "version": ver,
                    "release": rel,
                    "epoch": epoch,
                    "architecture": arch,
                }

    return None


def discover_gpu_model() -> Optional[str]:
    """Check for GPU model and return None if not found."""
    result = run_command("lspci | grep VGA", raise_on_error=False)

    if result.return_code != 0:
        _LOGGER.debug("No GPU model detected")
        _LOGGER.debug(
            "Unable to detect GPU model - 'lspci | grep VGA' returned non-zero version: %s",
            result.to_dict(),
        )
        return None

    gpu_model = "VGA" + result.stdout.splitlines()[0].split("VGA")[-1]
    _LOGGER.debug("GPU model detected: %s", gpu_model)

    return gpu_model


def discover_all() -> Dict[str, Any]:
    """Discover all the entries used in Thoth's configuration file."""
    result = {
        "cuda_version": discover_cuda_version(),
        "cudnn_version": discover_cudnn_version(),
        "python_version": discover_python_version(),
        "platform": discover_platform(),
        "base_image": discover_base_image(),
        "openmpi_version": discover_rpm_package("openmpi"),
        "openblas_version": discover_rpm_package("openblas"),
        "mkl_version": discover_mkl_version(),
    }

    os_name, os_version = discover_distribution()
    result["operating_system"] = {
        "name": os_name,
        "version": os_version,
    }

    result["hardware"] = {
        **{k: v or "null" for k, v in discover_cpu().items()},
        "gpu_model": discover_gpu_model() or "Unknown",
    }

    return result
