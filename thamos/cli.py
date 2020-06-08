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

"""Command line interface Thamos for interaction with Thoth."""

import logging
import typing
import os
import sys
from shutil import get_terminal_size
import json
from functools import wraps
from typing import Tuple
from typing import Optional

import yaml
from texttable import Texttable
import click
from termcolor import colored
import daiquiri
from thoth.python import Project
from thoth.common import ThothAdviserIntegrationEnum
from thamos.exceptions import NoProjectDirError
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


def _load_files(requirements_format: str) -> Tuple[str, Optional[str]]:
    """Load Pipfile/Pipfile.lock or requirements.in/txt from the current directory."""
    if requirements_format == "pipenv":
        project = Project.from_files(without_pipfile_lock=not os.path.exists("Pipfile.lock"))
    elif requirements_format in ("pip", "pip-tools", "pip-compile"):
        project = Project.from_pip_compile_files(allow_without_lock=True)
    else:
        raise ValueError(f"Unknown configuration option for requirements format: {requirements_format!r}")
    return project.pipfile.to_string(), project.pipfile_lock.to_string() if project.pipfile_lock else None


def _write_files(requirements: str, requirements_lock: str, requirements_format: str) -> None:
    """Write content of Pipfile/Pipfile.lock or requirements.in/txt to the current directory."""
    project = Project.from_dict(requirements, requirements_lock)
    if requirements_format == "pipenv":
        _LOGGER.debug("Writing to Pipfile/Pipfile.lock in %r", os.getcwd())
        project.to_files()
    elif requirements_format in ("pip", "pip-tools", "pip-compile"):
        _LOGGER.debug("Writing to requirements.in/requirements.txt in %r", os.getcwd())
        project.to_pip_compile_files()
        _LOGGER.debug("No changes to Pipfile to write")
    else:
        raise ValueError(
            f"Unknown requirements format, supported are 'pipenv' and 'pip': {requirements_format!r}"
        )


def _print_header(header: str) -> None:
    """Print header to terminal respecting terminal size."""
    terminal_size = get_terminal_size()
    padding = (terminal_size.columns - len(header) - 2) // 2
    click.echo(padding * " " + header)
    click.echo(padding * " " + "=" * len(header) + "  \n")


def _write_configuration(
    advised_configuration: dict,
    recommendation_type: str = None,
    limit_latest_versions: int = None,
    dev: bool = False,
) -> None:
    """Create thoth configuration file."""
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

    for idx, runtime_environment_entry in enumerate(
        content.get("runtime_environments", [])
    ):
        if runtime_environment_entry.get("name") == advised_configuration["name"]:
            _LOGGER.debug(
                "Adjusting configuration entry for %r based on recommendations",
                advised_configuration["name"],
            )
            runtime_environment_entry = advised_configuration
            if recommendation_type:
                runtime_environment_entry["recommendation_type"] = recommendation_type
            if limit_latest_versions:
                runtime_environment_entry[
                    "limit_latest_versions"
                ] = limit_latest_versions
            runtime_environment_entry["dev"] = dev
            content["runtime_environments"][idx] = runtime_environment_entry
            break
    else:
        _LOGGER.error(
            "Cannot adjust Thoth's configuration based on advises: No runtime environment entry with name %r found",
            advised_configuration["name"],
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
    """CLI tool for interacting with Thoth."""
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


@cli.command("version")
@click.pass_context
@click.option(
    "--json", "-j", "json_output", is_flag=True, help="Print output in JSON format."
)
def _print_version(ctx, json_output: bool = False):
    """Print Thamos and Thoth version and exit."""
    api_url = None
    thoth_version = None
    try:
        thoth_version = configuration.get_thoth_version()
        api_url = configuration.api_url
    except NoProjectDirError as exc:
        _LOGGER.warning("Cannot obtain Thoth backend information: %s", str(exc))

    if json_output:
        click.echo(
            json.dumps(
                {
                    "thamos_version": thamos_version,
                    "thoth_version": thoth_version,
                    "thoth_api_url": configuration.api_url,
                },
                indent=2,
            )
        )
    else:
        click.echo(f"Thamos Client version: {thamos_version!s}")
        click.echo(
            f"Thoth API {api_url if api_url is not None else 'N/A'}: {thoth_version if thoth_version else 'N/A'}"
        )

    ctx.exit(0)


@cli.command("advise")
@click.option(
    "--debug",
    is_flag=True,
    envvar="THAMOS_DEBUG",
    help="Run analysis in debug mode on Thoth.",
)
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
    envvar="THAMOS_RECOMMENDATION_TYPE",
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
    envvar="THAMOS_NO_STATIC_ANALYSIS",
    help="Do not perform static analysis of source code files.",
)
@click.option(
    "--json", "-j", "json_output", is_flag=True, help="Print output in JSON format."
)
@click.option(
    "--force",
    is_flag=True,
    envvar="THAMOS_FORCE",
    help="Force analysis run bypassing server-side cache.",
)
@click.option(
    "--runtime-environment",
    "-r",
    type=str,
    default=None,
    metavar="NAME",
    envvar="THAMOS_RUNTIME_ENVIRONMENT",
    help="Specify explicitly runtime environment to get recommendations for; "
    "defaults to the first entry in the configuration file.",
)
@click.option(
    "--limit-latest-versions",
    type=int,
    default=None,
    metavar="COUNT",
    envvar="THAMOS_LIMIT_LATEST_VERSIONS",
    help="Specify number of latest versions for each package to consider.",
)
@click.option(
    "--dev/--no-dev",
    envvar="THAMOS_DEV",
    is_flag=True,
    default=False,
    show_default=True,
    help="Consider or do not consider development dependencies during the resolution.",
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
    dev: bool = False,
):
    """Ask Thoth for recommendations on application stack."""
    with workdir():
        pipfile, pipfile_lock = _load_files(requirements_format=configuration.requirements_format)

        # In CLI we always call to obtain only the best software stack (count is implicitly set to 1).
        results = thoth_advise(
            pipfile,
            pipfile_lock,
            recommendation_type=recommendation_type,
            runtime_environment_name=runtime_environment,
            debug=debug,
            nowait=no_wait,
            force=force,
            source_type=ThothAdviserIntegrationEnum.CLI,
            limit_latest_versions=limit_latest_versions,
            no_static_analysis=no_static_analysis,
            dev=dev,
        )

        if not results:
            return sys.exit(2)

        if no_wait:
            # Echo the analysis id to user when not waiting.
            click.echo(results)
            sys.exit(0)

        result, error = results
        if error:
            if json_output:
                print({"error": result["error_msg"]})
            else:
                print(result["error_msg"])
            sys.exit(4)

        if not no_write:
            # Print report of the best one - thus index zero.
            if result["report"] and result["report"]["products"]:
                if result["report"]["products"][0]["justification"]:
                    _print_header("Recommended stack report")
                    _print_report(result["report"]["products"][0]["justification"], json_output=json_output)
                else:
                    click.echo("No justification was made for the recommended stack")

            if result["report"] and result["report"]["stack_info"]:
                _print_header("Application stack guidance")
                _print_report(result["report"]["stack_info"], json_output=json_output)

            pipfile = result["report"]["products"][0]["project"]["requirements"]
            pipfile_lock = result["report"]["products"][0]["project"]["requirements_locked"]
            _write_configuration(
                result["report"]["products"][0]["advised_runtime_environment"],
                recommendation_type,
                limit_latest_versions,
                dev,
            )
            _write_files(pipfile, pipfile_lock, configuration.requirements_format)
        else:
            click.echo(json.dumps(result, indent=2))

    sys.exit(0)


@cli.command("provenance-check")
@click.option(
    "--debug",
    is_flag=True,
    envvar="THAMOS_DEBUG",
    help="Run analysis in debug mode on Thoth.",
)
@click.option(
    "--json", "-j", "json_output", is_flag=True, help="Print output in JSON format."
)
@click.option(
    "--no-wait",
    is_flag=True,
    help="Do not wait for analysis to finish, just submit it.",
)
@click.option(
    "--force",
    is_flag=True,
    envvar="THAMOS_FORCE",
    help="Force analysis run bypassing server-side cache.",
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
        if configuration.requirements_format != "pipenv":
            raise ValueError("Provenance checks are available only for requirements managed by Pipenv")

        pipfile, pipfile_lock = _load_files("pipenv")
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
@click.argument("analysis_id", type=str, required=False)
def log(analysis_id: str = None):
    """Get log of running or finished analysis.

    If ANALYSIS_ID is not provided, there will be used last analysis id, if noted by Thamos.
    """
    if not analysis_id:
        with workdir():
            log_str = get_log()
    else:
        log_str = get_log(analysis_id)

    click.echo(log_str)


@cli.command("status")
@click.argument("analysis_id", type=str, required=False)
@click.option(
    "--output-format",
    "-o",
    type=click.Choice(["json", "yaml", "table"]),
    default="table",
    help="Specify output format for the status report.",
)
def status(analysis_id: str = None, output_format: str = None):
    """Get status of an analysis.

    If ANALYSIS_ID is not provided, there will be used last analysis id, if noted by Thamos.
    """
    if not analysis_id:
        with workdir():
            status_dict = get_status()
    else:
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
    if template:
        _LOGGER.info(
            "Creating configuration file from a configuration template %r", template
        )
        configuration.create_default_config(template)

        if not no_interactive:
            configuration.open_config_file()

        return

    if not configuration.config_file_exists():
        _LOGGER.info(
            "No configuration file found, creating one from a configuration template from %s",
            "a default template" if template is None else template,
        )
        configuration.create_default_config(template)

    if not no_interactive:
        configuration.open_config_file()
    elif no_interactive:
        _LOGGER.info(
            "Configuration file already present, no action performed in non-interactive mode"
        )


if __name__ == "__main__":
    cli()
