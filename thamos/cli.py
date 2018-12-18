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

"""Command line interface Thamos for interaction with Thoth."""

import logging
import typing
import os
import sys
from shutil import get_terminal_size
import json

import contoml as toml
from texttable import Texttable
import click
from termcolor import colored
import daiquiri
from thamos.config import config as configuration
from thamos.exceptions import NoProjectDirError
from thamos.exceptions import ThamosException
from thamos.lib import advise as thoth_advise
from thamos.lib import provenance_check as thoth_provenance_check
from thamos.utils import workdir
from thamos import __version__ as thamos_version

# Suppress anoying errors when name not known (disable_warnings() does not work here).
logging.getLogger('urllib3.connectionpool').setLevel(logging.ERROR)
daiquiri.setup(level=logging.INFO)
_LOGGER = logging.getLogger('thamos')

_EMOJI = {
    'WARNING': colored('\u26a0\ufe0f WARNING', 'yellow'),
    'ERROR': colored('\u274c ERROR', 'red', attrs=['bold']),
    'INFO': colored('\u2714\ufe0f INFO', 'green'),
    'LATEST': colored('\U0001f44c LATEST', 'green'),
    'CVE': colored('\u2620\uFE0F  CVE \u2620\uFE0F', 'red')
}

# Align of columns in table - default is left, values stated here are adjusted otherwise.
_TABLE_COLS_ALIGN = {
    'type': 'c',
    'severity': 'c',
    'package_name': 'c',
    'package_version': 'r'
}


def _print_version(ctx, _, value):
    """Print Kebechet version and exit."""
    if not value or ctx.resilient_parsing:
        return

    click.echo(thamos_version)
    ctx.exit()


def handle_cli_exception(func: typing.Callable) -> typing.Callable:
    """Suppress exception in CLI if debug mode was not turned on."""
    def wrapper(ctx, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            if ctx.parent.params['verbose']:
                raise

            _LOGGER.error(str(exc))
            sys.exit(1)

    return wrapper


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
        # TODO: enable prettify once https://github.com/jumpscale7/python-consistent-toml/issues/24 is fixed
        toml.dump(pipfile, 'Pipfile', prettify=False)
    else:
        _LOGGER.debug("No changes to Pipfile to write")

    if pipfile_lock:
        _LOGGER.debug("Writing to Pipfile.lock in %r", os.getcwd())
        with open('Pipfile.lock', 'w') as pipfile_lock_file:
            json.dump(pipfile_lock, pipfile_lock_file, sort_keys=True, indent=4)
    else:
        _LOGGER.debug("No changes to Pipfile.lock to write")


def _print_report(report: dict, json_output: bool = False):
    """Print reasoning to user."""
    if json_output:
        click.echo(json.dumps(report, sort_keys=True, indent=2))
        return

    table = Texttable(max_width=get_terminal_size().columns)
    table.set_deco(Texttable.HEADER | Texttable.VLINES)

    header = set()
    to_remove = set()
    for item in report:
        header = header.union(set(item.keys()))
        to_remove = to_remove.union(set(i for i, v in item.items() if isinstance(v, dict)))

    # Remove fields that can be an array - these are addition details that are supressed from the table output.
    header = header - to_remove

    header = list(sorted(header))
    table.set_cols_align([_TABLE_COLS_ALIGN.get(column, 'l') for column in header])
    table.header([item[0].upper() + item[1:].replace('_', ' ') for item in header])

    for item in report:
        row = []
        for column in header:
            entry = item.get(column, '-')

            if not bool(int(os.getenv('THAMOS_NO_EMOJI', 0))) and isinstance(entry, str):
                entry = _EMOJI.get(entry, entry)

            if isinstance(entry, list):
                entry = ", ".join(entry)

            row.append(entry)

        table.add_row(row)

    click.echo(table.draw())


@click.group()
@click.pass_context
@click.option('-v', '--verbose', is_flag=True, envvar='THAMOS_VERBOSE',
              help="Be verbose about what's going on.")
@click.option('--version', is_flag=True, is_eager=True, callback=_print_version, expose_value=False,
              help="Print version and exit.")
@click.option('--workdir', '-d', type=str, default=None,
              help="Adjust working directory for sub-commands.")
@click.option('--thoth-host', '-t', type=str, default=None,
              help="Use selected host instead of the one stated in the configuration file.")
def cli(ctx=None, verbose: bool = False, workdir: str = None, thoth_host: str = None):
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

    if thoth_host:
        configuration.explicit_host = thoth_host

    # Turn on progressbar explicitly here if it was not turned off by user. If Thamos is used
    # as a library, progressbar is not shown as one would expect.
    os.environ['THAMOS_NO_PROGRESSBAR'] = os.getenv('THAMOS_NO_PROGRESSBAR', '0')


@cli.command('advise')
@click.option('--debug', is_flag=True,
              help="Run analysis in debug mode on Thoth.")
@click.option('--no-write', '-W', is_flag=True,
              help="Do not write results to files, just print them.")
@click.option('--recommendation-type', '-r', type=str,
              help="Use selected recommendation type, do not load it from Thoth's config file.")
@click.option('--no-wait', is_flag=True,
              help="Do not wait for analysis to finish, just submit it.")
@click.option('--json', '-j', 'json_output', is_flag=True,
              help="Print output in JSON format.")
@click.option('--force', is_flag=True,
              help="Force analysis run bypassing server-side cache.")
def advise(debug: bool = False, no_write: bool = False, recommendation_type: str = None,
           no_wait: bool = False, json_output: bool = False, force: bool = False):
    """Update the given application stack and provide reasoning.."""
    with workdir():
        pipfile, pipfile_lock = _load_pipfiles()

        # In CLI we always call to obtain only the best software stack (count is implicitly set to 1).
        results = thoth_advise(
            pipfile,
            pipfile_lock,
            recommendation_type,
            debug=debug,
            nowait=no_wait,
            force=force
        )

        if not results:
            return sys.exit(2)

        if no_wait:
            # Echo the analysis id to user when not waiting.
            click.echo(results)
            sys.exit(0)

        report, error = results

        # Print report of the best one - thus index zero.
        _print_report(report[0][0], json_output=json_output)

        pipfile = report[0][1]['requirements']
        pipfile_lock = report[0][1]['requirements_locked']

        if not no_write:
            _write_pipfiles(pipfile, pipfile_lock)
        else:
            click.echo(pipfile)
            click.echo(pipfile_lock)

    sys.exit(4 if error else 0)


@cli.command('provenance-check')
@click.option('--debug', is_flag=True,
              help="Run analysis in debug mode on Thoth.")
@click.option('--json', '-j', 'json_output', is_flag=True,
              help="Print output in JSON format.")
@click.option('--no-wait', is_flag=True,
              help="Do not wait for analysis to finish, just submit it.")
@click.option('--force', is_flag=True,
              help="Force analysis run bypassing server-side cache.")
@click.pass_context
@handle_cli_exception
def provenance_check(debug: bool = False, no_wait: bool = False,
                     json_output: bool = False, force: bool = False):
    """Check provenance of installed packages."""
    with workdir():
        pipfile, pipfile_lock = _load_pipfiles()
        if not pipfile_lock:
            _LOGGER.error("No Pipfile.lock found - provenance cannot be checked")
            sys.exit(3)

        results = thoth_provenance_check(pipfile, pipfile_lock, debug=debug, nowait=no_wait, force=force)
        if not results:
            sys.exit(2)

        if no_wait:
            # Echo the analysis id to user when nowait.
            click.echo(results)
            sys.exit(0)

        report, error = results
        _print_report(report, json_output=json_output) if report else _LOGGER.info("Provenance check passed!")

        if error:
            sys.exit(5)

        if any(item.get('type') == 'ERROR' for item in report):
            sys.exit(4)

        return 0


@cli.command('config')
def config():
    """Adjust Thamos and Thoth remote configuration."""
    try:
        configuration.open_config_file()
    except NoProjectDirError:
        _LOGGER.info("No configuration file found, creating a default configuration for editing")
        configuration.create_default_config()
        configuration.open_config_file()


if __name__ == '__main__':
    cli()
