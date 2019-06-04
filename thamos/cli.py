#!/usr/bin/env python3
# thamos
# Copyright(C) 2018, 2019 Fridolin Pokorny
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
from functools import wraps

import contoml as toml
import yaml
from texttable import Texttable
import click
from termcolor import colored
import daiquiri
from thamos.config import config as configuration
from thamos.lib import advise as thoth_advise
from thamos.lib import provenance_check as thoth_provenance_check
from thamos.lib import get_log
from thamos.lib import get_status
from thamos.utils import workdir
from thamos import __version__ as thamos_version

# Suppress anoying errors when name not known (disable_warnings() does not work here).
logging.getLogger("urllib3.connectionpool").setLevel(logging.ERROR)
daiquiri.setup(level=logging.INFO)
_LOGGER = logging.getLogger("thamos")

_EMOJI = {
    "WARNING": colored("\u26a0\ufe0f WARNING", "yellow"),
    "ERROR": colored("\u274c ERROR", "red", attrs=["bold"]),
    "INFO": colored("\u2714\ufe0f INFO", "green"),
    "LATEST": colored("\U0001f44c LATEST", "green"),
    "CVE": colored("\u2620\uFE0F  CVE \u2620\uFE0F", "red"),
}

# Align of columns in table - default is left, values stated here are adjusted otherwise.
_TABLE_COLS_ALIGN = {
    "type": "c",
    "severity": "c",
    "package_name": "c",
    "package_version": "r",
}


def _print_version(ctx, _, value):
    """Print Kebechet version and exit."""
    if not value or ctx.resilient_parsing:
        return

    click.echo(thamos_version)
    ctx.exit()


def handle_cli_exception(func: typing.Callable) -> typing.Callable:
    """Suppress exception in CLI if debug mode was not turned on."""
    @wraps(func)
    def wrapper(ctx, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            if ctx.parent.params["verbose"]:
                raise

            _LOGGER.error(str(exc))
            sys.exit(1)

    return wrapper


def _load_pipfiles() -> tuple:
    """Load Pipfile and Pipfile.lock from the current directory."""
    _LOGGER.debug("Loading Pipfile in %r", os.getcwd())
    with open("Pipfile", "r") as pipfile_file:
        pipfile_content = pipfile_file.read()

    pipfile_lock_content = None
    try:
        _LOGGER.debug("Loading Pipfile.lock in %r", os.getcwd())
        with open("Pipfile.lock", "r") as pipfile_lock_file:
            pipfile_lock_content = pipfile_lock_file.read()
    except FileNotFoundError:
        _LOGGER.info("No Pipfile.lock found")

    return pipfile_content, pipfile_lock_content


def _write_pipfiles(pipfile: str, pipfile_lock: str) -> None:
    """Write content of Pipfile and Pipfile.lock to the current directory."""
    if pipfile:
        _LOGGER.debug("Writing to Pipfile in %r", os.getcwd())
        # TODO: enable prettify once https://github.com/jumpscale7/python-consistent-toml/issues/24 is fixed
        toml.dump(pipfile, "Pipfile", prettify=False)
    else:
        _LOGGER.debug("No changes to Pipfile to write")

    if pipfile_lock:
        _LOGGER.debug("Writing to Pipfile.lock in %r", os.getcwd())
        with open("Pipfile.lock", "w") as pipfile_lock_file:
            json.dump(pipfile_lock, pipfile_lock_file, sort_keys=True, indent=4)
    else:
        _LOGGER.debug("No changes to Pipfile.lock to write")


def _print_header(header: str) -> None:
    """Print header to terminal respecting terminal size."""
    terminal_size = get_terminal_size()
    padding = (terminal_size.columns - len(header) - 2) // 2
    click.echo(padding * " " + header)
    click.echo(padding * " " + "=" * len(header) + "  \n")


def _write_configuration(advised_configuration: dict, recommendation_type: str = None,
                         limit_latest_versions: int = None) -> None:
    if not advised_configuration:
        _LOGGER.debug("No advises on configuration, nothing to adjust")
        return

    if "name" not in advised_configuration:
        _LOGGER.error(
            "Cannot adjust Thoth's configuration based on advises: No name found in Thoth's configuration entry"
        )
        return

    _LOGGER.debug("Reading Thoth's configuration file")
    with open(".thoth.yaml", "r") as thoth_yaml_file:
        content = yaml.safe_load(thoth_yaml_file.read())

    for idx, runtime_environment_entry in enumerate(content.get("runtime_environments", [])):
        if runtime_environment_entry.get("name") == advised_configuration["name"]:
            _LOGGER.debug(
                "Adjusting configuration entry for %r based on recommendations",
                advised_configuration["name"]
            )
            runtime_environment_entry = advised_configuration
            if recommendation_type:
                runtime_environment_entry["recommendation_type"] = recommendation_type
            if limit_latest_versions:
                runtime_environment_entry["limit_latest_versions"] = limit_latest_versions
            content["runtime_environments"][idx] = runtime_environment_entry
            break
    else:
        _LOGGER.error(
            "Cannot adjust Thoth's configuration based on advises: No runtime environment entry with name %r found",
            advised_configuration["name"]
        )
        return

    _LOGGER.debug("Writing adjusted Thoth's configuration file")
    with open(".thoth.yaml", "w") as thoth_yaml_file:
        yaml.safe_dump(content, thoth_yaml_file)


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
        to_remove = to_remove.union(
            set(i for i, v in item.items() if isinstance(v, dict))
        )

    # Remove fields that can be an array - these are addition details that are supressed from the table output.
    header = header - to_remove

    header = list(sorted(header))
    table.set_cols_align([_TABLE_COLS_ALIGN.get(column, "l") for column in header])
    table.header([item[0].upper() + item[1:].replace("_", " ") for item in header])

    for item in report:
        row = []
        for column in header:
            entry = item.get(column, "-")

            if not bool(int(os.getenv("THAMOS_NO_EMOJI", 0))) and isinstance(
                entry, str
            ):
                entry = _EMOJI.get(entry, entry)

            if isinstance(entry, list):
                entry = ", ".join(entry)

            row.append(entry)

        table.add_row(row)

    click.echo(table.draw())


@click.group()
@click.pass_context
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    envvar="THAMOS_VERBOSE",
    help="Be verbose about what's going on.",
)
@click.option(
    "--version",
    is_flag=True,
    is_eager=True,
    callback=_print_version,
    expose_value=False,
    help="Print version and exit.",
)
@click.option(
    "--workdir",
    "-d",
    type=str,
    default=None,
    help="Adjust working directory for sub-commands.",
)
@click.option(
    "--thoth-host",
    "-t",
    type=str,
    default=None,
    help="Use selected host instead of the one stated in the configuration file.",
)
def cli(ctx=None, verbose: bool = False, workdir: str = None, thoth_host: str = None):
    """A CLI tool for interacting with Thoth."""
    if ctx:
        ctx.auto_envvar_prefix = "THAMOS"

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
    os.environ["THAMOS_NO_PROGRESSBAR"] = os.getenv("THAMOS_NO_PROGRESSBAR", "0")


@cli.command("advise")
@click.option("--debug", is_flag=True, help="Run analysis in debug mode on Thoth.")
@click.option(
    "--no-write",
    "-W",
    is_flag=True,
    help="Do not write results to files, just print them.",
)
@click.option(
    "--recommendation-type",
    "-t",
    type=str,
    metavar="RECOMMENDATION_TYPE",
    help="Use selected recommendation type, do not load it from Thoth's config file.",
)
@click.option(
    "--no-wait",
    is_flag=True,
    help="Do not wait for analysis to finish, just submit it.",
)
@click.option(
    "--no-static-analysis",
    is_flag=True,
    help="Do not perform static analysis of source code files.",
)
@click.option(
    "--json", "-j", "json_output", is_flag=True, help="Print output in JSON format."
)
@click.option(
    "--force", is_flag=True, help="Force analysis run bypassing server-side cache."
)
@click.option(
    "--runtime-environment",
    "-r",
    type=str,
    default=None,
    metavar="NAME",
    help="Specify explicitly runtime environment to get recommendations for; "
    "defaults to the first entry in the configuration file.",
)
@click.option(
    "--limit-latest-versions",
    type=int,
    default=None,
    metavar="COUNT",
    help="Specify number of latest versions for each package to consider.",
)
def advise(
    debug: bool = False,
    no_write: bool = False,
    recommendation_type: str = None,
    runtime_environment: str = None,
    no_wait: bool = False,
    no_static_analysis: bool = False,
    json_output: bool = False,
    limit_latest_versions: int = None,
    force: bool = False,
):
    """Ask Thoth for recommendations on application stack."""
    with workdir():
        pipfile, pipfile_lock = _load_pipfiles()

        # In CLI we always call to obtain only the best software stack (count is implicitly set to 1).
        results = thoth_advise(
            pipfile,
            pipfile_lock,
            recommendation_type=recommendation_type,
            runtime_environment_name=runtime_environment,
            debug=debug,
            nowait=no_wait,
            force=force,
            limit_latest_versions=limit_latest_versions,
            no_static_analysis=no_static_analysis,
        )

        if not results:
            return sys.exit(2)

        if no_wait:
            # Echo the analysis id to user when not waiting.
            click.echo(results)
            sys.exit(0)

        result, error = results

        if not no_write:
            # Print report of the best one - thus index zero.
            if result["report"][0][0]:
                _print_header("Recommended stack report")
                _print_report(result["report"][0][0], json_output=json_output)

            if result["stack_info"]:
                _print_header("Application stack guidance")
                _print_report(result["stack_info"], json_output=json_output)

            if not error:
                pipfile = result["report"][0][1]["requirements"]
                pipfile_lock = result["report"][0][1]["requirements_locked"]
                _write_configuration(result["advised_configuration"], recommendation_type, limit_latest_versions)
                _write_pipfiles(pipfile, pipfile_lock)
        else:
            click.echo(json.dumps(result, indent=2))

        if error:
            sys.exit(4)

    sys.exit(0)


@cli.command("provenance-check")
@click.option("--debug", is_flag=True, help="Run analysis in debug mode on Thoth.")
@click.option(
    "--json", "-j", "json_output", is_flag=True, help="Print output in JSON format."
)
@click.option(
    "--no-wait",
    is_flag=True,
    help="Do not wait for analysis to finish, just submit it.",
)
@click.option(
    "--force", is_flag=True, help="Force analysis run bypassing server-side cache."
)
@click.pass_context
@handle_cli_exception
def provenance_check(
    debug: bool = False,
    no_wait: bool = False,
    json_output: bool = False,
    force: bool = False,
):
    """Check provenance of installed packages."""
    with workdir():
        pipfile, pipfile_lock = _load_pipfiles()
        if not pipfile_lock:
            _LOGGER.error("No Pipfile.lock found - provenance cannot be checked")
            sys.exit(3)

        results = thoth_provenance_check(
            pipfile, pipfile_lock, debug=debug, nowait=no_wait, force=force
        )
        if not results:
            sys.exit(2)

        if no_wait:
            # Echo the analysis id to user when nowait.
            click.echo(results)
            sys.exit(0)

        report, error = results
        _print_report(report, json_output=json_output) if report else _LOGGER.info(
            "Provenance check passed!"
        )

        if error:
            sys.exit(5)

        if any(item.get("type") == "ERROR" for item in report):
            sys.exit(4)

        return 0


@cli.command("log")
@click.argument("analysis_id", type=str)
def log(analysis_id: str):
    """Get log of running or finished analysis."""
    click.echo(get_log(analysis_id))


@cli.command("status")
@click.argument("analysis_id", type=str)
@click.option(
    "--output-format",
    "-o",
    type=click.Choice(["json", "yaml", "table"]),
    default="table",
    help="Specify output format for the status report.",
)
def status(analysis_id: str, output_format: str = None):
    """Get status of an analysis."""
    status_dict = get_status(analysis_id)
    if not output_format or output_format == "table":
        table = Texttable(max_width=get_terminal_size().columns)
        table.set_deco(Texttable.VLINES)
        table.add_rows(list(status_dict.items()), header=False)
        output = table.draw()
    elif output_format == "json":
        output = json.dumps(status_dict, indent=2)
    elif output_format == "yaml":
        output = yaml.safe_dump(status_dict, default_flow_style=False)
    else:
        raise NotImplementedError(f"Unknown output format {output_format}")

    click.echo(output)


@cli.command("config")
@click.option(
    "--no-interactive",
    "-I",
    envvar="THAMOS_NO_INTERACTIVE",
    is_flag=True,
    help="Do not open editor with configuration.",
)
@click.option(
    "--template",
    "-t",
    metavar="FILE",
    type=str,
    envvar="THAMOS_CONFIG_TEMPLATE",
    help="Template which should be used instead of the default one.",
)
def config(no_interactive: bool = False, template: str = None):
    """Adjust Thamos and Thoth remote configuration.

    Perform autodiscovery of available hardware and software on the host and
    create a default configuration for Thoth (placed into .thoth.yaml).
    """
    if not configuration.config_file_exists():
        _LOGGER.info(
            "No configuration file found, creating one from a default configuration template"
        )
        configuration.create_default_config(template)
    elif no_interactive:
        _LOGGER.info("Configuration file already present, no action performed in non-interactive mode")

    if not no_interactive:
        configuration.open_config_file()


if __name__ == "__main__":
    cli()
