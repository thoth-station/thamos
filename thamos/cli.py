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

"""The CLI."""

import logging
import os

import click
import daiquiri
from thamos.config import config as configuration
from thamos.exceptions import NoProjectDirError
from thamos.lib import advise as thoth_advise
from thamos.lib import provenance_check as thoth_provenance_check
from thamos.utils import workdir
from thamos import __version__ as thamos_version

daiquiri.setup(level=logging.INFO)
_LOGGER = logging.getLogger('thamos')


def _print_version(ctx, _, value):
    """Print Kebechet version and exit."""
    if not value or ctx.resilient_parsing:
        return

    click.echo(thamos_version)
    ctx.exit()


def _load_pipfiles() -> tuple:
    """Load Pipfile and Pipfile.lock from the current directory."""
    _LOGGER.debug("Loading Pipfile in %r", os.getcwd())
    with open('Pipfile', 'r') as pipfile_file:
        pipfile_content = pipfile_file.read()

    pipfile_lock_content = None
    try:
        _LOGGER.debug("Loading Pipfile.lock in %r", os.getcwd())
        with open('Pipfile.lock', 'r') as pipfile_lock_file:
            pipfile_lock_content = pipfile_lock_file.read()
    except FileNotFoundError:
        _LOGGER.info("No Pipfile.lock found")

    return pipfile_content, pipfile_lock_content


def _write_pipfiles(pipfile: str, pipfile_lock: str):
    """Write content of Pipfile and Pipfile.lock to the current directory."""
    if pipfile:
        _LOGGER.debug("Writing to Pipfile in %r", os.getcwd())
        with open('Pipfile', 'w') as pipfile_file:
            pipfile_file.write(pipfile)
    else:
        _LOGGER.debug("No changes to Pipfile to write")

    if pipfile_lock:
        _LOGGER.debug("Writing to Pipfile.lock in %r", os.getcwd())
        with open('Pipfile.lock', 'w') as pipfile_lock_file:
            pipfile_lock_file.write(pipfile_lock)
    else:
        _LOGGER.debug("No changes to Pipfile.lock to write")


def _print_reasoning(reasoning: dict):
    """Print reasoning to user."""
    # TODO: improve this to have a more human readable output.
    from pprint import pprint
    pprint(reasoning)


@click.group()
@click.pass_context
@click.option('-v', '--verbose', is_flag=True, envvar='THAMOS_VERBOSE',
              help="Be verbose about what's going on.")
@click.option('--version', is_flag=True, is_eager=True, callback=_print_version, expose_value=False,
              help="Print version and exit.")
@click.option('--workdir', type=str, default=None,
              help="Adjust working directory for sub-commands.")
def cli(ctx=None, verbose: bool = False, workdir: str = None):
    """A CLI tool for interacting with Thoth."""
    if ctx:
        ctx.auto_envvar_prefix = 'THAMOS'

    if verbose:
        _LOGGER.setLevel(logging.DEBUG)
        _LOGGER.debug("Debug mode turned on")
        _LOGGER.debug("Thamos version: %r", thamos_version)

    if workdir:
        _LOGGER.debug("Changing working directory into %r", workdir)
        os.chdir(workdir)


@cli.command('advise')
@click.option('--debug', is_flag=True, auto_envvar_prefix=True,
              help="Run analysis in debug mode on Thoth.")
def advise(debug: bool = False):
    """Update the given application stack and provide reasoning.."""
    with workdir():
        pipfile, pipfile_lock = _load_pipfiles()

        pipfile, pipfile_lock, reasoning = thoth_advise(
            pipfile, pipfile_lock, debug)

        _print_reasoning(reasoning)
        _write_pipfiles(pipfile, pipfile_lock)


@cli.command('provenance-check')
@click.option('--debug', is_flag=True, auto_envvar_prefix=True,
              help="Run analysis in debug mode on Thoth.")
def provenance_check(debug: bool = False):
    """Check provenance of installed packages."""
    with workdir():
        pipfile, pipfile_lock = _load_pipfiles()
        if not pipfile_lock:
            _LOGGER.error(
                "No Pipfile.lock found - provenance cannot be checked")
            return 1

        pipfile, pipfile_lock, reasoning = thoth_provenance_check(
            pipfile, pipfile_lock, debug)

        _print_reasoning(reasoning)
        _write_pipfiles(pipfile, pipfile_lock)


@cli.command('image-analysis')
def image_analysis():
    """Submit the given image for analysis in Thoth."""
    raise NotImplementedError


@cli.command('config')
def config():
    """Adjust Thamos and Thoth remote configuration."""
    try:
        configuration.open_config_file()
    except NoProjectDirError:
        _LOGGER.info(
            "No configuration file found, creating a default configuration for editing")
        configuration.create_default_config()
        configuration.open_config_file()


if __name__ == '__main__':
    cli()
