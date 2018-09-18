#!/usr/bin/env python3
# thamos
# Copyright(C) 2018 Fridolin Pokorny
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
import json

import distro
import click
from thoth.analyzer import run_command
from thoth.adviser.python import Source

from .utils import workdir
from .config import config

_LOGGER = logging.getLogger(__name__)


def discover_cuda_version(interactive: bool = False) -> typing.Optional[str]:
    """Check for CUDA version, if no CUDA is installed, return None."""
    if bool(int(os.getenv('THAMOS_DISABLE_CUDA', 0))):
        _LOGGER.debug(
            "Disabling CUDA based on THAMOS_DISABLE_CUDA environment variable that is set to %r",
            os.environ['THAMOS_DISABLE_CUDA']
        )
        return None

    result = run_command('nvcc --version', raise_on_error=False)
    if result.return_code != 0:
        _LOGGER.debug("Unable to detect CUDA version - nvcc returned non-zero version: %s", result.to_dict())
        return None

    lines = result.stdout.splitlines()
    version_info = lines[-1].split(',')
    if len(version_info) != 3:
        _LOGGER.debug("Unable to detect CUDA version from nvcc output: %r", result.stdout)
        return None

    cuda_version = version_info[1].strip()[len('release '):]

    if interactive:
        cuda_version = click.prompt('Please select CUDA version', default=cuda_version)

    _LOGGER.debug("Detected CUDA version: %r", cuda_version)
    return cuda_version


def discover_distribution() -> tuple:
    """Get distribution identifier and distribution version."""
    distro.linux_distribution
    distribution, version, *_ = distro.linux_distribution(full_distribution_name=False)
    return distribution, version


def discover_python_version() -> tuple:
    """Discover Python version in which we run in."""
    return sys.version_info.major, sys.version_info.minor
