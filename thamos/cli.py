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
import json
from functools import wraps
from typing import Tuple
from typing import Optional
from typing import Set

import yaml
import click
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich import box
import daiquiri
import micropipenv
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
    "WARNING": Text("\u26a0\ufe0f WARNING", style="yellow"),
    "ERROR": Text("\u274c ERROR", style="bold red"),
    "INFO": Text("\u2714\ufe0f INFO", "green"),
    "LATEST": Text("\U0001f44c LATEST", "cyan"),
    "CVE": Text("\u2620\uFE0F  CVE \u2620\uFE0F", "red"),
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
    # noqa
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
        project = Project.from_files(
            without_pipfile_lock=not os.path.exists("Pipfile.lock")
        )
    elif requirements_format in ("pip", "pip-tools", "pip-compile"):
        project = Project.from_pip_compile_files(allow_without_lock=True)
    else:
        raise ValueError(
            f"Unknown configuration option for requirements format: {requirements_format!r}"
        )
    return (
        project.pipfile.to_string(),
        project.pipfile_lock.to_string() if project.pipfile_lock else None,
    )


def _write_files(
    requirements: str, requirements_lock: str, requirements_format: str
) -> None:
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


def _write_configuration(
    advised_configuration: dict,
    recommendation_type: str = None,
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


def _print_report(report: dict, json_output: bool = False, title: Optional[str] = None):
    """Print reasoning to user."""
    if json_output:
        click.echo(json.dumps(report, sort_keys=True, indent=2))
        return

    console = Console()
    table = Table(
        show_header=True,
        header_style="bold green",
        title=title,
        box=box.MINIMAL_DOUBLE_HEAD,
    )

    header = set()  # type: Set[str]
    to_remove = set()  # type: Set[str]
    for item in report:
        header = header.union(set(item.keys()))
        to_remove = to_remove.union(
            set(i for i, v in item.items() if isinstance(v, dict))
        )

    # Remove fields that can be an array - these are addition details that are supressed from the table output.
    header = header - to_remove

    header_list = list(sorted(header))
    for item in header_list:
        table.add_column(
            item.replace("_", " ").capitalize(), style="cyan", overflow="fold"
        )

    for item in report:
        row = []
        for column in header_list:
            entry = item.get(column, "-")

            if not bool(int(os.getenv("THAMOS_NO_EMOJI", 0))) and isinstance(
                entry, str
            ):
                entry = _EMOJI.get(entry, entry)

            if isinstance(entry, list):
                entry = ", ".join(entry)

            if isinstance(entry, str) and entry.startswith(("https://", "http://")):
                entry = f"[link {entry}]{entry}"

            row.append(entry)

        table.add_row(*row)

    console.print(table, justify="center")


class AliasedGroup(click.Group):
    """Provide clever command aliases."""

    def get_command(self, ctx, cmd_name):
        """Get command to be executed based on the prefix.

        https://click.palletsprojects.com/en/7.x/advanced/#command-aliases
        """
        if cmd_name == "logs":
            # Address `thamos logs` vs `thamos log` confusion.
            cmd_name = "log"

        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx) if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail("Too many matches: %s" % ", ".join(sorted(matches)))


@click.group(cls=AliasedGroup)
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


@cli.command("install")
@click.option(
    "--dev/--no-dev",
    is_flag=True,
    default=False,
    envvar="THAMOS_DEV",
    show_default=True,
    help="Consider or do not consider development dependencies during the installation process.",
)
def install(dev: bool) -> None:
    """Install dependencies as stated in Pipfile.lock or requirements.txt.

    This command assumes requirements files are present and dependencies are already resolved.
    If that's not the case, issue `thamos advise` before calling this.
    """
    with workdir():
        method = (
            "pipenv"
            if configuration.requirements_format == "pipenv"
            else "requirements"
        )
        micropipenv.install(method=method, deploy=True, dev=dev)


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
    "--no-user-stack",
    is_flag=True,
    help="Do not submit lock file with the request, this lock file is normally used as a base for "
    "comparision to recommend a better stack than the one used.",
    envvar="THAMOS_NO_USER_STACK",
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
    "--dev/--no-dev",
    envvar="THAMOS_DEV",
    is_flag=True,
    default=False,
    show_default=True,
    help="Consider or do not consider development dependencies during the resolution.",
)
@click.option(
    "--install",
    envvar="THAMOS_INSTALL",
    is_flag=True,
    default=False,
    show_default=True,
    help="Install dependencies once the advise is done.",
)
def advise(
    debug: bool = False,
    no_write: bool = False,
    recommendation_type: str = None,
    runtime_environment: str = None,
    no_wait: bool = False,
    no_static_analysis: bool = False,
    json_output: bool = False,
    force: bool = False,
    dev: bool = False,
    no_user_stack: bool = False,
    install: bool = False,
):
    """Ask Thoth for recommendations on application stack."""
    if install and no_wait:
        _LOGGER.error("Cannot install dependencies as --no-wait was provided")
        sys.exit(1)
    if install and no_write:
        _LOGGER.error("Cannot install dependencies if lock files are not written")
        sys.exit(1)

    with workdir():
        pipfile, pipfile_lock = _load_files(
            requirements_format=configuration.requirements_format
        )

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
            no_static_analysis=no_static_analysis,
            dev=dev,
            no_user_stack=no_user_stack,
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
                json.dump(result, sys.stdout, indent=2)
            else:
                stack_info = (result.get("report") or {}).get("stack_info")
                if stack_info:
                    _print_report(
                        stack_info,
                        json_output=json_output,
                        title="Application stack guidance",
                    )
                print(
                    result.get("error_msg")
                    or "No error message was provided by the service."
                )

            sys.exit(4)

        if not no_write:
            if result["report"] and result["report"]["stack_info"]:
                _print_report(
                    result["report"]["stack_info"],
                    json_output=json_output,
                    title="Application stack guidance",
                )

            # Print report of the best one - thus index zero.
            if result["report"] and result["report"]["products"]:
                if result["report"]["products"][0]["justification"]:
                    _print_report(
                        result["report"]["products"][0]["justification"],
                        json_output=json_output,
                        title="Recommended stack report",
                    )
                else:
                    click.echo("No justification was made for the recommended stack")

            pipfile = result["report"]["products"][0]["project"]["requirements"]
            pipfile_lock = result["report"]["products"][0]["project"][
                "requirements_locked"
            ]
            _write_configuration(
                result["report"]["products"][0]["advised_runtime_environment"],
                recommendation_type,
                dev,
            )
            _write_files(pipfile, pipfile_lock, configuration.requirements_format)  # type: ignore

            if install:
                method = (
                    "pipenv"
                    if configuration.requirements_format == "pipenv"
                    else "requirements"
                )
                micropipenv.install(method=method, deploy=True, dev=dev)
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
            raise ValueError(
                "Provenance checks are available only for requirements managed by Pipenv"
            )

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
        if report:
            _print_report(
                report, json_output=json_output, title="Provenance check report"
            )
        else:
            _LOGGER.info("Provenance check passed!")

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
        table = Table()

        for key in status_dict.keys():
            table.add_column(
                key.replace("_", " ").capitalize(),
                style="cyan",
                overflow="fold",
            )

        table.add_row(*status_dict.values())

        console = Console()
        console.print(table, justify="center")
        return
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
