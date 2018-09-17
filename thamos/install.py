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

"""Implementation of a custom installation procedure to setup environment."""

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


def _get_cuda_version(interactive: bool = False) -> typing.Optional[str]:
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


def install_tensorflow(version: str = None, interactive: bool = False):
    """Install TensorFlow respecting the given host configuration."""
    _LOGGER.debug("Installing TensorFlow")
    distro.linux_distribution
    distribution, version, *_ = distro.linux_distribution(full_distribution_name=False)
    distribution = distribution + version
    _LOGGER.debug("Detected distribution: %r", distribution)
    if interactive:
        distribution = click.prompt('Please select distribution', default=distribution)

    cuda_version = _get_cuda_version(interactive)

    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    if interactive:
        python_version = click.prompt('Please select Python version', default=python_version)

    pipenv_python_version = 'three' if python_version.startswith('3') else 'two'
    # TODO: verify_ssl based on config
    index = config.index_aicoe['base_url'] + '/fedora28/1.9/jemalloc/simple'
    result = run_command(
        f'pipenv install --{pipenv_python_version} tensorflow -i {index}', raise_on_error=False
    )
    # TODO: get URL to index based on config + check if installed artifact is from our index
    with workdir('Pipfile.lock'):
        # Now check if the installed tensorflow is actaully from aicoe index.
        with open('Pipfile.lock', 'r') as pipfile_lock:
            source = Source.from_dict(json.load(pipfile_lock))


def do_install(packages: typing.List[str], interactive: bool = False) -> list:
    """Perform installation of packages"""
    for package in packages:
        # TODO: parse version strings
        version = None
        package = package.lower()
        func = INSTALLATION_PROCEDURE[package]
        _LOGGER.debug("Installation of %r in version %r, using procedure %r", package, version, func)
        func(version, interactive)


INSTALLATION_PROCEDURE = {
    'tensorflow': install_tensorflow
}
