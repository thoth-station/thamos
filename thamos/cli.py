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

import json
import logging
import os
import shutil
import subprocess
import sys
import typing
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
from micropipenv import HashMismatch
from thoth.common import cwd
from thoth.common import ThothAdviserIntegrationEnum
from thoth.common import get_justification_link as jl
from thamos.exceptions import NoProjectDirError
from thamos.exceptions import NoRuntimeEnvironmentError
from thamos.config import config as configuration
from thamos.lib import advise_here as thoth_advise_here
from thamos.lib import provenance_check as thoth_provenance_check
from thamos.lib import list_hardware_environments
from thamos.lib import list_python_package_indexes
from thamos.lib import list_thoth_s2i
from thamos.lib import get_log
from thamos.lib import install as thamos_install
from thamos.lib import get_status
from thamos.lib import write_configuration, write_files, load_files
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

    header_list = sorted(header)
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
def cli(
    ctx=None,
    verbose: bool = False,
    workdir: str = typing.Optional[None],
    thoth_host: str = None,
):
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
    except Exception as exc:
        if _LOGGER.getEffectiveLevel() <= logging.DEBUG:
            _log = _LOGGER.exception
        else:
            _log = _LOGGER.error

        _log("Failed to obtain Thoth backend version: %s", str(exc))

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
@click.pass_context
@click.option(
    "--dev/--no-dev",
    is_flag=True,
    default=False,
    envvar="THAMOS_DEV",
    show_default=True,
    help="Consider or do not consider development dependencies during the installation process.",
)
@click.option(
    "--runtime-environment",
    "-r",
    type=str,
    default=None,
    metavar="NAME",
    envvar="THAMOS_RUNTIME_ENVIRONMENT",
    help="Specify explicitly runtime environment for which the installation process should be done.",
)
@click.argument("pip_args", nargs=-1)
@handle_cli_exception
def install(runtime_environment: str, dev: bool, pip_args: Tuple[str]) -> None:
    """Install dependencies as stated in the lock file.

    This command assumes requirements files are present and dependencies are already resolved.
    If that's not the case, issue `thamos advise` before running this command.

    Examples:
      thamos install --runtime-environment "testing"

      thamos install --dev

      thamos install --no-dev -- --force-reinstall
    """
    try:
        thamos_install(
            runtime_environment_name=runtime_environment, dev=dev, pip_args=pip_args
        )
    except HashMismatch as exc:
        _LOGGER.error(
            "Changes made to packages are not reflected in the lock file, please install "
            "using `thamos advise --install` to apply changes made: %s",
            str(exc),
        )


def _error_virtual_environment(virtualenv_path: str) -> None:
    """Print error and exit if virtual environment was not setup."""
    if not os.path.isdir(virtualenv_path):
        if configuration.content.get("virtualenv", False):
            _LOGGER.error(
                "No virtual environment created yet, create it using `thamos install`"
            )
        else:
            _LOGGER.error(
                "No virtual environment management configured, use `thamos config` to adjust configuration"
            )

        sys.exit(1)


@cli.command("run")
@click.argument("command", nargs=-1, metavar="CMD")
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
def run(command: typing.List[str], runtime_environment: Optional[str] = None) -> None:
    """Run the command in virtual environment.

    Examples:
      thamos run ./app.py

      thamos run --runtime-environment "testing" -- flask --help
    """
    virtualenv_path = configuration.get_virtualenv_path(runtime_environment)
    if virtualenv_path is None:
        _LOGGER.error("No virtual environment found for %r", runtime_environment)
        sys.exit(1)

    python_path = os.path.join(virtualenv_path, "bin", "python3")
    _error_virtual_environment(virtualenv_path)
    # No magic here.
    cmd = [python_path, *command]
    subprocess.run(cmd, universal_newlines=True, check=True)


@cli.command("venv")
@click.pass_context
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
def venv(ctx, runtime_environment: Optional[str] = None) -> None:
    """Get path of the virtual environment."""
    virtualenv_path = configuration.get_virtualenv_path(runtime_environment)
    if virtualenv_path is None:
        _LOGGER.error("No virtual environment found")
        ctx.exit(1)
    _error_virtual_environment(virtualenv_path)
    print(virtualenv_path)


@cli.command("purge")
@click.pass_context
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
    "--all",
    "-A",
    is_flag=True,
    help="Purge virtual environments for all the runtime environments configured.",
)
def purge(ctx, runtime_environment: Optional[str] = None, all: bool = False) -> None:
    """Remove virtual environment created.

    Examples:
      thamos purge

      thamos purge --runtime-environment "testing"

      thamos purge --all
    """
    if all:
        for runtime_environment_config in configuration.list_runtime_environments():
            _LOGGER.warning(
                "Removing virtual environment for %r",
                runtime_environment_config["name"],
            )
            path = configuration.get_virtualenv_path(runtime_environment)
            if path is None:
                _LOGGER.warning(
                    "No virtual environment for %r found",
                    runtime_environment_config["name"],
                )
                continue
            shutil.rmtree(
                path,
                ignore_errors=True,
            )
    else:
        runtime_environment_config = configuration.get_runtime_environment(
            runtime_environment
        )
        _LOGGER.warning(
            "Removing virtual environment for %r", runtime_environment_config["name"]
        )
        path = configuration.get_virtualenv_path(runtime_environment)
        if path is None:
            _LOGGER.error(
                "No virtual environment for %r found",
                runtime_environment_config["name"],
            )
            ctx.exit(1)
        shutil.rmtree(path, ignore_errors=True)


@cli.command("advise")
@click.pass_context
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
@click.option(
    "--write-advised-manifest-changes",
    envvar="THAMOS_WRITE_ADVISED_MANIFEST_CHANGES",
    type=str,
    metavar="FILE",
    default=None,
    show_default=True,
    help="Write advised manifest changes to a file.",
)
@handle_cli_exception
def advise(
    debug: bool = False,
    no_write: bool = False,
    recommendation_type: typing.Optional[str] = None,
    runtime_environment: typing.Optional[str] = None,
    no_wait: bool = False,
    no_static_analysis: bool = False,
    json_output: bool = False,
    force: bool = False,
    dev: bool = False,
    no_user_stack: bool = False,
    install: bool = False,
    write_advised_manifest_changes: Optional[str] = None,
):
    """Ask Thoth for recommendations on the application stack.

    Ask the remote Thoth service for advise on the application stack used. The command
    collects information stated in the .thoth.yaml file for the given runtime environment,
    static source code analysis and requirements for the application and sends them to the
    remote service. Optionally, install packages resolved by Thoth.

    Examples:
      thamos advise --runtime-environment "testing"

      thamos advise --dev

      thamos advise --install

      thamos advise --no-static-analysis --no-user-stack
    """
    if install and no_wait:
        _LOGGER.error("Cannot install dependencies as --no-wait was provided")
        sys.exit(1)
    if install and no_write:
        _LOGGER.error("Cannot install dependencies if lock files are not written")
        sys.exit(1)

    with cwd(configuration.get_overlays_directory(runtime_environment)):
        if not dev and configuration.requirements_format == "pipenv":
            _LOGGER.warning(
                "Development dependencies will not be considered during the resolution process - see %s",
                jl("no_dev"),
            )

        # In CLI we always call to obtain only the best software stack (count is implicitly set to 1).
        results = thoth_advise_here(
            recommendation_type=recommendation_type,
            src_path=configuration.config_path,
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
            write_configuration(
                result["report"]["products"][0]["advised_runtime_environment"],
                recommendation_type,
                dev,
            )
            write_files(pipfile, pipfile_lock, configuration.requirements_format)  # type: ignore

            if write_advised_manifest_changes:
                advised_manifest_changes = result["report"]["products"][0][
                    "project"
                ].get("advised_manifest_changes")
                with open(
                    write_advised_manifest_changes, "w"
                ) as advised_manifest_changes_file:
                    json.dump(
                        advised_manifest_changes or {}, advised_manifest_changes_file
                    )
                    advised_manifest_changes_file.write("\n")

            if install:
                thamos_install(runtime_environment_name=runtime_environment, dev=dev)
        else:
            click.echo(json.dumps(result, indent=2))

    sys.exit(0)


@cli.command("provenance-check")
@click.pass_context
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
    "--force",
    is_flag=True,
    envvar="THAMOS_FORCE",
    help="Force analysis run bypassing server-side cache.",
)
@handle_cli_exception
def provenance_check(
    debug: bool = False,
    no_wait: bool = False,
    json_output: bool = False,
    force: bool = False,
    runtime_environment: typing.Optional[str] = None,
):
    """Check provenance of installed packages.

    Collect information about direct dependencies and dependencies stated in the lock file
    and send them to the remote service to verify their provenance.

    Examples:
      thamos provenance-check --runtime-environment "production"
    """
    with cwd(configuration.get_overlays_directory(runtime_environment)):
        if configuration.requirements_format != "pipenv":
            raise ValueError(
                "Provenance checks are available only for requirements managed by Pipenv"
            )

        pipfile, pipfile_lock = load_files("pipenv")
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
@click.pass_context
@click.argument("analysis_id", type=str, required=False, metavar="ANALYSIS_ID")
@handle_cli_exception
def log(analysis_id: typing.Optional[str] = None):
    """Get log of running or finished analysis.

    If ANALYSIS_ID is not provided, the last request is used by default.
    """
    if not analysis_id:
        with workdir():
            log_str = get_log()
    else:
        log_str = get_log(analysis_id)

    click.echo(log_str)


@cli.command("status")
@click.pass_context
@click.argument("analysis_id", type=str, required=False, metavar="ANALYSIS_ID")
@click.option(
    "--output-format",
    "-o",
    type=click.Choice(["json", "yaml", "table"]),
    default="table",
    help="Specify output format for the status report.",
)
@handle_cli_exception
def status(
    analysis_id: typing.Optional[str] = None, output_format: typing.Optional[str] = None
):
    """Get status of an analysis.

    If ANALYSIS_ID is not provided, the last request is used by default.

    Examples:
      thamos status

      thamos status "adviser-940101080006-110c392feb7cf6da"
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


@cli.command("list")
@click.pass_context
@handle_cli_exception
def list_() -> None:
    """List available runtime environments configured.

    Examples:
      thamos list
    """
    with workdir(configuration.CONFIG_NAME):
        environments = configuration.list_runtime_environments()

    if not environments:
        _LOGGER.error("No runtime environments found")
        sys.exit(1)

    for env in environments:
        click.echo(env.get("name"))


@cli.command("show")
@click.pass_context
@click.option(
    "--output-format",
    "-o",
    type=click.Choice(["json", "yaml"]),
    default="yaml",
    help="Specify output format for the status report.",
    show_default=True,
)
@click.option(
    "--runtime-environment",
    "-r",
    type=str,
    default=None,
    metavar="NAME",
    envvar="THAMOS_RUNTIME_ENVIRONMENT",
    help="Specify explicitly runtime environment to be shown.",
)
@handle_cli_exception
def show(output_format: str, runtime_environment: Optional[str] = None) -> None:
    """Show details for configured runtime environments.

    Examples:
      thamos show --runtime-environment "development"
    """
    with workdir(configuration.CONFIG_NAME):
        environments = configuration.list_runtime_environments()

    if not runtime_environment:
        if not environments:
            _LOGGER.error("No runtime environments found")
            sys.exit(1)

    to_show = environments
    if runtime_environment:
        for env in environments:
            if env.get("name") == runtime_environment:
                to_show = env
                break
        else:
            raise NoRuntimeEnvironmentError(
                f"Runtime environment {runtime_environment!r} not found"
            )

    if output_format == "json":
        output = json.dumps(to_show, indent=2)
    elif output_format == "yaml":
        output = yaml.safe_dump(to_show, default_flow_style=False)
    else:
        raise NotImplementedError(f"Unknown output format {output_format}")

    click.echo(output)


@cli.command("config")
@click.pass_context
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
@handle_cli_exception
def config(no_interactive: bool = False, template: str = None):
    """Adjust Thamos and Thoth configuration.

    Open the .thoth.yaml configuration file. If does not exist yet, perform
    auto-discovery of available hardware and software on the host and
    create a default configuration for Thoth.
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


@cli.command("check")
@click.pass_context
@click.option(
    "--runtime-environment",
    "-r",
    type=str,
    default=None,
    metavar="NAME",
    envvar="THAMOS_RUNTIME_ENVIRONMENT",
    help="Specify explicitly runtime environment to check configuration file against.",
)
@click.option(
    "--output-format",
    "-o",
    type=click.Choice(["json", "yaml", "table"]),
    default="table",
    help="Specify output format for the status report.",
)
@handle_cli_exception
def check(runtime_environment: Optional[str], output_format: str) -> None:
    """Check the configuration file and runtime environment.

    Check the correctness of the configuration file and runtime environment configuration
    for the current host.

    Examples:
        thamos check --runtime-environment "production"

        thamos check --output-format yaml
    """
    result = configuration.check(runtime_environment_name=runtime_environment)

    if output_format == "yaml":
        yaml.safe_dump(result, sys.stdout)
    elif output_format == "json":
        json.dump(result, sys.stdout, indent=2)
        sys.stdout.write("\n")
    elif output_format == "table":
        table = Table()

        header = set()
        for item in result:
            for key in item.keys():
                header.add(key)

        header_sorted = sorted(header)
        for item in header_sorted:
            table.add_column(
                item.replace("_", " ").capitalize(),
                style="cyan",
                overflow="fold",
            )

        for item in result:
            row = []
            for key in header_sorted:
                entry = item.get(key)
                if not bool(int(os.getenv("THAMOS_NO_EMOJI", 0))) and isinstance(
                    entry, str
                ):
                    entry = _EMOJI.get(entry, entry)

                row.append(entry if entry is not None else "-")

            table.add_row(*row)

        console = Console()
        console.print(table, justify="center")

    sys.exit(1 if any(item.get("type") == "ERROR" for item in result) else 0)


@cli.command("s2i")
@click.pass_context
@click.option(
    "--output-format",
    "-o",
    type=click.Choice(["json", "yaml", "table"]),
    default="table",
    help="Specify output format for the status report.",
)
@handle_cli_exception
def s2i(output_format: str) -> None:
    """Check available Thoth Source-To-Image containers.

    Examples:
      thamos s2i --output-format json
    """
    result = list_thoth_s2i()

    if output_format == "yaml":
        yaml.safe_dump({"s2i": result}, sys.stdout)
    elif output_format == "json":
        json.dump({"s2i": result}, sys.stdout, indent=2)
        sys.stdout.write("\n")
    elif output_format == "table":
        table = Table()

        header = set()
        for item in result:
            for key in item.keys():
                header.add(key)

        header_sorted = sorted(header)
        header_sorted.append("info")
        for item in header_sorted:
            table.add_column(
                item.replace("_", " ").capitalize(),
                style="cyan",
                overflow="fold",
            )

        for item in result:
            row = []
            for key in header_sorted:
                if key == "info":
                    image_name = item.get("thoth_s2i_image_name")
                    row.append(jl(image_name.rsplit("/", maxsplit=1)[-1]))
                    continue

                entry = item.get(key)
                row.append(str(entry) if entry is not None else "-")

            table.add_row(*row)

        console = Console()
        console.print(table, justify="center")

    sys.exit(1 if any(item.get("type") == "ERROR" for item in result) else 0)


@cli.command("hw")
@click.pass_context
@click.option(
    "--output-format",
    "-o",
    type=click.Choice(["json", "yaml", "table"]),
    default="table",
    help="Specify output format for the status report.",
)
@handle_cli_exception
def hw(output_format: str) -> None:
    """List available hardware information on backend.

    List available hardware information on the backend for which resolver can give more detailed information.
    This hardware configuration is not enforced and is find if it does not match the one available on the
    client side.
    """
    result = list_hardware_environments()

    if output_format == "yaml":
        yaml.safe_dump({"hw": result}, sys.stdout)
    elif output_format == "json":
        json.dump({"hw": result}, sys.stdout, indent=2)
        sys.stdout.write("\n")
    elif output_format == "table":
        table = Table()

        header = set()
        for item in result:
            for key in item.keys():
                header.add(key)

        header_sorted = sorted(header)
        for item in header_sorted:
            table.add_column(
                item.replace("_", " ")
                .replace("cpu", "CPU")
                .replace("gpu", "GPU")
                .replace("ram", "RAM"),
                style="cyan",
                overflow="fold",
            )

        for item in result:
            row = []
            for key in header_sorted:
                entry = item.get(key)
                row.append(str(entry) if entry is not None else "-")

            table.add_row(*row)

        console = Console()
        console.print(table, justify="center")

    sys.exit(0)


@cli.command("indexes")
@click.pass_context
@click.option(
    "--output-format",
    "-o",
    type=click.Choice(["json", "yaml", "table"]),
    default="table",
    help="Specify output format for the status report.",
)
@handle_cli_exception
def indexes(output_format: str) -> None:
    """List available Python package indexes."""
    result = list_python_package_indexes()

    if output_format == "yaml":
        yaml.safe_dump({"indexes": result}, sys.stdout)
    elif output_format == "json":
        json.dump({"indexes": result}, sys.stdout, indent=2)
        sys.stdout.write("\n")
    elif output_format == "table":
        table = Table()

        header = set()
        for item in result:
            for key in item.keys():
                if key == "warehouse_api_url":
                    continue
                header.add(key)

        header_sorted = sorted(header)
        for item in header_sorted:
            table.add_column(
                item.capitalize()
                .replace("_", " ")
                .replace("Url", "URL")
                .replace("ssl", "SSL")
                .replace("api", "API")
            )

        for item in result:
            row = []
            for key in header_sorted:
                entry = item.get(key)
                row.append(str(entry) if entry is not None else "-")

            table.add_row(*row)

        console = Console()
        console.print(table, justify="center")

    sys.exit(0)


@cli.command("add")
@click.pass_context
@click.argument("requirement", nargs=-1, metavar="PKG")
@click.option(
    "--runtime-environment",
    "-r",
    default=None,
    metavar="NAME",
    envvar="THAMOS_RUNTIME_ENVIRONMENT",
    help="Specify runtime environment to which the given package should be added.",
)
@click.option(
    "--index-url",
    "-i",
    default="https://pypi.org/simple",
    type=str,
    metavar="INDEX_URL",
    show_default=True,
    help="Specify Python package index to be used as a source for the given requirement.",
)
@click.option(
    "--dev",
    is_flag=True,
    show_default=True,
    help="Add the given package to the development packages.",
)
@handle_cli_exception
def add(
    requirement: typing.List[str],
    runtime_environment: typing.Optional[str],
    index_url: str,
    dev: bool,
) -> None:
    """Add one or multiple requirements to the project.

    Add one or multiple requirements to the direct dependency listing without actually installing them.
    The supplied requirement is specified using PEP-508 standard.

    Examples:
      thamos add flask

      thamos add tensorflow --runtime-environment "training"

      thamos add --dev 'pytest~=6.2.0'

      thamos add 'importlib-metadata; python_version < "3.8"'
    """
    project = configuration.get_project(runtime_environment, missing_dir_ok=True)
    for req in requirement:
        _LOGGER.info(
            "Adding %r to %s requirements of runtime environment %r",
            req,
            "development" if dev else "default",
            project.runtime_environment.name,
        )
        project.pipfile.add_requirement(
            req, is_dev=dev, index_url=index_url, force=True
        )

    _LOGGER.warning(
        "Changes done might require triggering new advise to resolve dependencies"
    )
    configuration.save_project(project)


@cli.command("remove")
@click.pass_context
@click.argument("requirement", nargs=-1, metavar="PKG")
@click.option(
    "--runtime-environment",
    "-r",
    default=None,
    metavar="NAME",
    envvar="THAMOS_RUNTIME_ENVIRONMENT",
    help="Specify runtime environment from which the given package should be removed.",
)
@handle_cli_exception
def remove(
    requirement: typing.List[str],
    runtime_environment: typing.Optional[str],
) -> None:
    """Remove the given requirement.

    Examples:
      thamos remove flask

      thamos remove pytest --runtime-environment "training"
    """
    project = configuration.get_project(runtime_environment)

    for req in requirement:
        any_change = False
        if req in project.pipfile.packages.packages:
            project.pipfile.packages.packages.pop(req)
            _LOGGER.info(
                "Removed %r from default requirements for runtime environment %r",
                req,
                project.runtime_environment.name,
            )
            any_change = True

        if req in project.pipfile.dev_packages.packages:
            project.pipfile.dev_packages.packages.pop(req)
            _LOGGER.info(
                "Removed %r from development requirements for runtime environment %r",
                req,
                project.runtime_environment.name,
            )
            any_change = True

        if not any_change:
            _LOGGER.error(
                "Requirement %r not found in project requirements for runtime environment %r, "
                "aborting making any changes",
                req,
                project.runtime_environment.name,
            )
            sys.exit(1)

    _LOGGER.warning(
        "Changes done might require triggering new advise to resolve dependencies"
    )
    configuration.save_project(project)


__name__ == "__main__" and cli()
