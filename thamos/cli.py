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

"""Command line interface Thamos for interaction with Thoth."""

import json
import logging
import os
import shutil
import subprocess
import sys
import typing
from collections import OrderedDict
from functools import wraps
from typing import Dict
from typing import Optional
from typing import Set
from typing import Tuple

import yaml
import rich_click as click
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich import box
import daiquiri
from micropipenv import HashMismatch
from thoth.common import cwd
from thoth.common import ThothAdviserIntegrationEnum
from thoth.common import get_justification_link as jl
from thamos.exceptions import ConfigurationError
from thamos.exceptions import NoProjectDirError
from thamos.exceptions import NoRuntimeEnvironmentError
from thamos.exceptions import RequirementsFileError
from thamos.config import config as configuration
from thamos.lib import advise_here as thoth_advise_here
from thamos.lib import add_requirements_to_project
from thamos.lib import collect_support_information_dict
from thamos.lib import check_runtime_environment_run
from thamos.lib import get_log
from thamos.lib import get_package_from_imported_packages
from thamos.lib import get_status
from thamos.lib import get_last_analysis_id
from thamos.lib import install as thamos_install
from thamos.lib import list_python_package_indexes
from thamos.lib import list_python_environments
from thamos.lib import list_thoth_container_images
from thamos.lib import load_dot_env
from thamos.lib import load_files
from thamos.lib import provenance_check as thoth_provenance_check
from thamos.lib import print_dependency_graph
from thamos.lib import print_advise_results
from thamos.lib import get_verified_packages_from_static_analysis
from thamos.lib import write_configuration
from thamos.lib import write_files
from thamos.utils import workdir
from thamos.cli_config import init_rich_click
from thamos import __version__ as thamos_version

# Suppress anoying errors when name not known (disable_warnings() does not work here).
logging.getLogger("urllib3.connectionpool").setLevel(logging.ERROR)
daiquiri.setup(level=logging.INFO)
_LOGGER = logging.getLogger("thamos")
init_rich_click()

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


_REPORT_TRANSLATION_TABLE_INDEXES = {
    "url": "Python package index URL",
    "verify_ssl": "Verify SSL",
}


_REPORT_TRANSLATION_TABLE_IMAGES = {
    "cuda_version": "CUDA version",
    "datetime": "Analysis datetime",
    "env_image_name": "Image name",
    "env_image_tag": "Image tag",
    "environment_name": "Environment name",
    "environment_type": "Environment type",
    "image_sha": "Container image SHA",
    "os_name": "OS name",
    "os_version": "OS version",
    "package_extract_document_id": "Container image analysis",
    "python_version": "Python version",
    "thoth_image_name": "Thoth container image name",
    "thoth_image_version": "Thoth container image version",
}


_REPORT_TRANSLATION_TABLE_WHATPROVIDES = {
    "package_import": "Package import",
    "index_url": "Python package index URL",
    "package_name": "Python package name",
    "package_version": "Python package version",
}


_REPORT_TRANSLATION_TABLE_ENVIRONMENTS = {
    "os_name": "Operating system name",
    "os_version": "Operating system version",
    "python_version": "Python version",
}

_REPORT_TRANSLATION_TABLE_SCORECARD_TAGS = {
    "binary-artifacts": "projects have binary artifacts in the source repository",
    "no-binary-artifacts": "projects do NOT have binary artifacts in the source repository",
    "unfixed-vulnerabilities": "projects have open or unfixed vulnerabilities on the OSV service",
    "no-unfixed-vulnerabilities": "projects do NOT have open or unfixed vulnerabilities on the OSV service",
    "code-review": "projects require code review before the code is merged",
    "no-code-review": "projects do NOT require code review before the code is merged",
    "actively-maintained": "projects are actively maintained",
    "no-actively-maintained": "projects are NOT actively maintained",
    "automatic-updates": "projects use use tools for automatic dependency updates",
    "no-automatic-updates": "projects do NOT use use tools for automatic dependency updates",
    "branch-protection": "projects have branch protection setup",
    "no-branch-protection": "projects do NOT have branch protection setup",
    "least-privileged-workflow": "projects follow the principle of least privileged in GitHub workflows",
    "no-least-privileged-workflow": "projects do NOT follow the principle of least privileged in GitHub workflows",
    "security-policy": "projects have a security policy published",
    "no-security-policy": "projects do NOT have a security policy published",
    "signed-releases": "projects cryptographically sign released artifacts",
    "no-signed-releases": "projects do NOT cryptographically sign released artifacts",
    "fuzzing": "projects use fuzzing",
    "no-fuzzing": "projects do NOT use fuzzing",
    "published-package": "projects are published as packages",
    "no-published-package": "projects are NOT published as packages",
    "cii": "projects follow best CII practices",
    "no-cii": "projects do NOT follow best CII practices",
    "pinned-dependencies": "projects use pinned dependencies",
    "no-pinned-dependencies": "projects do NOT use pinned dependencies",
    "multiple-companies-contributors": "projects have a set of contributors from multiple companies",
    "no-multiple-companies-contributors": "projects do NOT have a set of contributors from multiple companies",
    "ci-tests": "projects run CI tests before pull requests are merged",
    "no-ci-tests": "projects do NOT run CI tests before pull requests are merged",
    "static-analysis": "projects use static source code analysis",
    "no-static-analysis": "projects do NOT use static source code analysis",
    "dangerous-patterns": "projects GitHub Action workflows have dangerous code patterns",
    "no-dangerous-patterns": "projects GitHub Action workflows do NOT have dangerous code patterns",
    "license": "projects have published a license",
    "no-license": "projects have NOT published a license",
    "webhook-token": "projects have a token for webhooks configured in their"
    " repository to authenticate the origins of requests",
    "no-webhook-token": "projects do NOT have a token for webhooks configured in their"
    " repository to authenticate the origins of requests",
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


def _print_report(
    report: list,
    *,
    json_output: bool = False,
    title: Optional[str] = None,
    show_header: bool = True,
    translation_table: Optional[Dict[str, str]] = None,
):
    """Print reasoning to user."""
    if json_output:
        click.echo(json.dumps(report, sort_keys=True, indent=2))
        return

    console = Console()
    table = Table(
        show_header=show_header,
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

    translation_table = translation_table or {}
    header_list = sorted(header)
    for item in header_list:
        item = translation_table.get(item) or item.replace("_", " ").capitalize()
        table.add_column(item, overflow="fold")

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


def _print_report_summary(analysis_id: str, report: list, *, json_output: bool = False):
    """Print reasoning to user."""
    if json_output:
        click.echo(json.dumps(report, sort_keys=True, indent=2))
        return

    console = Console()

    types = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for item in report:
        types[item["type"]] += 1

    console.print("Short Summary", justify="center", style="bold")
    console.print(
        f"The advise analysis fished with {types['INFO']} INFO messages, {types['WARNING']} WARNING messages,"
        + f" and {types['ERROR']} ERROR messages.",
        justify="center",
    )
    console.print(
        "Results can be browsed in Thoth search: [link https://thoth-station.ninja/search/advise/"
        + f"{analysis_id}]https://thoth-station.ninja/search/advise/{analysis_id}",
        justify="center",
    )


def _parse_labels(label: Optional[str]) -> Optional[Dict[str, str]]:
    """Parse labels from their string representation."""
    if not label:
        return None

    labels: Dict[str, str] = {}
    parts = label.split(";")
    for part in parts:
        lab = part.split("=")
        if len(lab) != 2:
            raise ValueError(f"Unknown label, expected key=val: {part}")

        if lab[0] in labels:
            raise ValueError(f"Duplicate label {lab[0]!r}")

        if not lab[0]:
            raise ValueError(f"Empty label key for label value {lab[1]!r}")

        if not lab[1]:
            raise ValueError(f"Empty label value for label key {lab[0]!r}")

        labels[lab[0]] = lab[1]

    return labels


def _print_advise_justifications(
    result,
    json_output: bool = False,
):
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

    return None


def _compute_metrics_scorecards(report) -> Optional[OrderedDict]:
    """Aggregate OSSF Scorecards information from report and compute metrics."""
    nb_dependencies = 0
    scorecards_metrics = {}

    if report["products"] and report["products"][0]["dependency_graph"]["nodes"]:
        nb_dependencies = len(report["products"][0]["dependency_graph"]["nodes"])

    for justification in report["products"][0]["justification"]:
        if "scorecard" in justification["link"]:
            if "tag" in justification:
                message = _REPORT_TRANSLATION_TABLE_SCORECARD_TAGS[justification["tag"]]

            # TO DO: Remove when corresponding prescriptions have been updated with tags
            else:
                replacement_words = {
                    "Project ": "projects ",
                    " is ": " are ",
                    " does ": " do ",
                    " has ": " have ",
                    " runs ": " run ",
                    " requires ": " require ",
                    " uses ": " use ",
                    " follows ": " follow ",
                    " signs ": " sign ",
                    " NOT ": " not ",
                }
                message = justification["message"].strip()

                for k, v in replacement_words.items():
                    message = message.replace(k, v)

            message = message.split("based")[0]

            if message not in scorecards_metrics:
                scorecards_metrics[message] = 1

            else:
                scorecards_metrics[message] += 1

    if scorecards_metrics != {}:

        # TO DO: find a better sorting logic based on tags
        return OrderedDict(
            sorted(
                {
                    k: int(v * nb_dependencies / 100)
                    for k, v in scorecards_metrics.items()
                }.items(),
                key=lambda t: "not" in t[0],
            )
        )

    return None


class AliasedGroup(click.RichGroup):
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
    metavar="DIR",
    type=str,
    default=None,
    help="Adjust working directory for sub-commands.",
)
@click.option(
    "--thoth-host",
    "-t",
    metavar="HOST",
    type=str,
    default=None,
    help="Use selected host instead of the one stated in the configuration file.",
)
def cli(
    ctx=None,
    verbose: bool = False,
    workdir: typing.Optional[str] = None,
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
def install(
    runtime_environment: str, dev: bool, pip_args: Tuple[str]
) -> None:  # noqa: D412
    """Install dependencies as stated in the lock file.

    This command assumes requirements files are present and dependencies are already resolved.
    If that's not the case, issue `thamos advise` before running this command.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos install --runtime-environment testing

      thamos install --dev

      thamos install --no-dev -- --force-reinstall
    [/purple]
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
@click.option(
    "--no-pedantic/--pedantic",
    "-P",
    is_flag=True,
    show_default=True,
    envvar="THAMOS_RUN_NO_PEDANTIC",
    help="Do not abort running the application if the runtime environment used does not match configuration.",
)
def run(
    command: typing.List[str],
    runtime_environment: Optional[str] = None,
    no_pedantic: bool = False,
) -> None:  # noqa: D412
    """Run the command in virtual environment.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos run ./app.py

      thamos run --runtime-environment stage -- flask --help

      thamos run --runtime-environment testing --no-pedantic -- ./train.py
    [/purple]
    """
    virtualenv_path = configuration.get_virtualenv_path(runtime_environment)
    if virtualenv_path is None:
        _LOGGER.error("No virtual environment found for %r", runtime_environment)
        sys.exit(1)

    overlays_dir = configuration.get_overlays_directory(runtime_environment)

    if not no_pedantic:
        check_runtime_environment_run(
            configuration.get_runtime_environment(runtime_environment)
        )

        if configuration.requirements_format == "pipenv":
            project = configuration.get_project(runtime_environment)

            if not project.pipfile_lock:
                raise RequirementsFileError(
                    f"No Pipfile.lock found, lock your dependencies using `{sys.argv[0]} advise`"
                )

            if project.pipfile.hash() != project.pipfile_lock.meta.hash:
                raise RequirementsFileError(
                    f"Pipfile hash does not correspond to the lock file hash, use `{sys.argv[0]} advise` "
                    f"to lock your dependencies"
                )

            _LOGGER.info("Pipfile hash corresponds to the hash stated in the lock file")
        else:
            _LOGGER.warning(
                "Cannot verify requirements hash as Pipenv files are not used"
            )

    process_env = dict(os.environ)
    if (
        overlays_dir
    ):  # Load any .env in the overlays directory or top root project directory.
        process_env = {
            **process_env,
            **load_dot_env(os.path.join(overlays_dir, ".env")),
        }

    python_path = os.path.join(virtualenv_path, "bin", "python3")
    _error_virtual_environment(virtualenv_path)
    # No magic here.
    cmd = [python_path, *command]
    _LOGGER.debug("Running application using %r", cmd)
    subprocess.run(cmd, universal_newlines=True, check=True, env=process_env)


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
    else:
        _error_virtual_environment(virtualenv_path)

    click.echo(virtualenv_path)


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
def purge(
    ctx, runtime_environment: Optional[str] = None, all: bool = False
) -> None:  # noqa: D412
    """Remove virtual environment created.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos purge

      thamos purge --runtime-environment testing

      thamos purge --all
    [/purple]
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
        if not path:
            _LOGGER.error(
                "No virtual environment for %r found",
                runtime_environment_config["name"],
            )
            ctx.exit(1)
        else:
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
    "--short",
    is_flag=True,
    help="Shorten the analysis output.",
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
@click.option(
    "--labels",
    "-l",
    envvar="THAMOS_LABELS",
    type=str,
    metavar="KEY1=VALUE1;KEY2=VALUE2,VALUE3",
    default=None,
    show_default=True,
    help="Labels used to label the request.",
)
@click.option(
    "--scoring",
    envvar="THAMOS_SHOW_METRICS",
    type=str,
    is_flag=True,
    default=False,
    show_default=True,
    help="Experimental feature: show Thoth package scoring based on OSSF Security Scorecards",
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
    short: bool = False,
    force: bool = False,
    dev: bool = False,
    no_user_stack: bool = False,
    install: bool = False,
    labels: Optional[str] = None,
    scoring: bool = False,
    write_advised_manifest_changes: Optional[str] = None,
) -> None:  # noqa: D412
    """Ask Thoth for recommendations on the application stack.

    Ask the remote Thoth service for advise on the application stack used. The command
    collects information stated in the .thoth.yaml file for the given runtime environment,
    static source code analysis and requirements for the application and sends them to the
    remote service. Optionally, install packages resolved by Thoth.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos advise --runtime-environment testing --labels 'foo=bar;qux=baz,bap'

      thamos advise --dev

      thamos advise --install

      thamos advise --no-static-analysis --no-user-stack
    [/purple]
    """
    if install and no_wait:
        _LOGGER.error("Cannot install dependencies as --no-wait was provided")
        sys.exit(1)
    if install and no_write:
        _LOGGER.error("Cannot install dependencies if lock files are not written")
        sys.exit(1)

    labels_dict = _parse_labels(labels)

    if not dev and configuration.requirements_format == "pipenv":
        _LOGGER.warning(
            "Development dependencies will not be considered during the resolution process - see %s",
            jl("no_dev"),
        )

    # In CLI we always call to obtain only the best software stack (count is implicitly set to 1).
    results = thoth_advise_here(
        recommendation_type=recommendation_type,
        src_path=".",
        runtime_environment_name=runtime_environment,
        debug=debug,
        nowait=no_wait,
        force=force,
        source_type=ThothAdviserIntegrationEnum.CLI,
        no_static_analysis=no_static_analysis,
        dev=dev,
        no_user_stack=no_user_stack,
        verify_tls=configuration.tls_verify,
        labels=labels_dict,
    )

    if not results:
        sys.exit(2)

    if no_wait:
        # Echo the analysis id to user when not waiting.
        click.echo(results)
        sys.exit(0)

    result, error, metadata = results
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

            Console().print(
                result.get("error_msg")
                or "No error message was provided by the service.",
                style="bold red",
                justify="center",
            )

        sys.exit(4)
    if not no_write:
        with cwd(configuration.get_overlays_directory(runtime_environment)):
            if json_output:
                _print_report(
                    result["report"],
                    json_output=json_output,
                )

            else:
                if short:
                    _print_report_summary(
                        metadata.document_id,
                        result["report"]["stack_info"],
                        json_output=json_output,
                    )
                else:
                    _print_advise_justifications(result, json_output=json_output)

                if scoring:
                    scorecards_metrics = _compute_metrics_scorecards(result["report"])
                    if scorecards_metrics:
                        Console().print(
                            "Based on OSSF Security Scorecards ( https://github.com/ossf/scorecard ) :\n\n"
                        )
                        for message, metric in scorecards_metrics.items():
                            Console().print(f"- {metric}% of {message}\n")

            pipfile = result["report"]["products"][0]["project"]["requirements"]
            pipfile_lock = result["report"]["products"][0]["project"][
                "requirements_locked"
            ]
            write_configuration(
                result["report"]["products"][0]["advised_runtime_environment"],
                recommendation_type,
                dev,
            )
            write_files(pipfile, pipfile_lock, configuration.requirements_format)

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
) -> None:  # noqa: D412
    """Check provenance of installed packages.

    Collect information about direct dependencies and dependencies stated in the lock file
    and send them to the remote service to verify their provenance.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos provenance-check --runtime-environment production
    [/purple]
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


@cli.command("log")
@click.pass_context
@click.argument("analysis_id", type=str, required=False, metavar="ANALYSIS_ID")
@click.option(
    "--runtime-environment",
    "-r",
    default=None,
    metavar="NAME",
    envvar="THAMOS_RUNTIME_ENVIRONMENT",
    help="Specify runtime environment to which the given package should be added.",
)
@handle_cli_exception
def log(
    analysis_id: typing.Optional[str] = None,
    runtime_environment: typing.Optional[str] = None,
):
    """Get log of running or finished analysis.

    If ANALYSIS_ID is not provided, the last request is used by default.
    """
    if not analysis_id:
        with cwd(configuration.get_overlays_directory(runtime_environment)):
            log_str = get_log()
    else:
        log_str = get_log(analysis_id)

    click.echo(log_str)


@cli.command("status")
@click.pass_context
@click.argument("analysis_id", type=str, required=False, metavar="ANALYSIS_ID")
@click.option(
    "--runtime-environment",
    "-r",
    default=None,
    metavar="NAME",
    envvar="THAMOS_RUNTIME_ENVIRONMENT",
    help="Specify runtime environment to which the given package should be added.",
)
@click.option(
    "--output-format",
    "-o",
    type=click.Choice(["json", "yaml", "table"]),
    default="table",
    help="Specify output format for the status report.",
)
@handle_cli_exception
def status(
    analysis_id: typing.Optional[str] = None,
    output_format: typing.Optional[str] = None,
    runtime_environment: typing.Optional[str] = None,
) -> None:  # noqa: D412
    """Get status of an analysis.

    If ANALYSIS_ID is not provided, the last request is used by default.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos status

      thamos status adviser-940101080006-110c392feb7cf6da
    [/purple]
    """
    if not analysis_id:
        with cwd(configuration.get_overlays_directory(runtime_environment)):
            analysis_id = get_last_analysis_id()

    status_dict = get_status(analysis_id)

    if not output_format or output_format == "table":
        _print_report(
            [status_dict],
            json_output=False,
            title=f"The current status for {analysis_id!r}",
        )
        return
    elif output_format == "json":
        output = json.dumps(status_dict, indent=2)
    elif output_format == "yaml":
        output = yaml.safe_dump(status_dict, default_flow_style=False)
    else:
        raise NotImplementedError(f"Unknown output format {output_format}")

    click.echo(output)


@cli.command("graph")
@click.pass_context
@click.argument("analysis_id", type=str, required=False, metavar="ANALYSIS_ID")
@click.option(
    "--fold/--unfold",
    is_flag=True,
    envvar="THAMOS_GRAPH_FOLD",
    default=True,
    type=bool,
    help="Collapse repeating sub-graphs in the output.",
)
@click.option(
    "--runtime-environment",
    "-r",
    default=None,
    metavar="NAME",
    envvar="THAMOS_RUNTIME_ENVIRONMENT",
    help="Specify runtime environment to which the given package should be added.",
)
@handle_cli_exception
def graph(
    analysis_id: typing.Optional[str] = None,
    runtime_environment: typing.Optional[str] = None,
    fold: bool = True,
) -> None:  # noqa: D412
    """Show dependency graph of resolved dependencies.

    If ANALYSIS_ID is not provided, the last request is used by default.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos graph

      thamos graph adviser-940101080006-110c392feb7cf6da
    [/purple]
    """
    with cwd(configuration.get_overlays_directory(runtime_environment)):
        printed = print_dependency_graph(analysis_id, fold=fold)
        if not printed:
            sys.exit(1)


@cli.command("results")
@click.pass_context
@click.argument("analysis_id", type=str, required=False, metavar="ANALYSIS_ID")
@click.option(
    "--json", "-j", "json_output", is_flag=True, help="Print output in JSON format."
)
@click.option(
    "--runtime-environment",
    "-r",
    default=None,
    metavar="NAME",
    envvar="THAMOS_RUNTIME_ENVIRONMENT",
    help="Specify runtime environment used to retrieve analysis results.",
)
@handle_cli_exception
def results(
    analysis_id: typing.Optional[str] = None,
    runtime_environment: typing.Optional[str] = None,
    json_output: bool = False,
) -> None:  # noqa: D412
    """Show results of finished adviser analysis.

    If ANALYSIS_ID is not provided, the last request is used by default.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos results

      thamos results adviser-940101080006-110c392feb7cf6da
    [/purple]
    """
    with cwd(configuration.get_overlays_directory(runtime_environment)):
        result = print_advise_results(analysis_id)

        _print_advise_justifications(result, json_output=json_output)


@cli.command("list")
@click.pass_context
@handle_cli_exception
def list_() -> None:  # noqa: D412
    """List available runtime environments configured.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos list
    [/purple]
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
def show(
    output_format: str, runtime_environment: Optional[str] = None
) -> None:  # noqa: D412
    """Show details for configured runtime environments.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos show --runtime-environment development
    [/purple]
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
def check(runtime_environment: Optional[str], output_format: str) -> None:  # noqa: D412
    """Check the configuration file and runtime environment.

    Check the correctness of the configuration file and runtime environment configuration
    for the current host.

    [bold yellow]Examples:[/bold yellow]
    [purple]

        thamos check --runtime-environment production

        thamos check --output-format yaml
    [/purple]
    """
    result = configuration.check(runtime_environment_name=runtime_environment)

    if result:
        if output_format == "yaml":
            yaml.safe_dump(result, sys.stdout)
        elif output_format == "json":
            json.dump(result, sys.stdout, indent=2)
            sys.stdout.write("\n")
        elif output_format == "table":
            _print_report(
                result,
                json_output=False,
                title="Runtime environment and configuration check results",
            )

    return_code = 1 if any(item.get("type") == "ERROR" for item in result) else 0
    if return_code == 0:
        _LOGGER.info("Configuration check passed!")

    sys.exit(return_code)


@cli.command("images")
@click.pass_context
@click.option(
    "--output-format",
    "-o",
    type=click.Choice(["json", "yaml", "table"]),
    default="table",
    help="Specify output format for the status report.",
)
@click.option(
    "--os-name",
    "-n",
    type=str,
    default=None,
    metavar="OS_NAME",
    help="Operating system name filter.",
)
@click.option(
    "--os-version",
    "-v",
    type=str,
    default=None,
    metavar="OS_VERSION",
    help="Operating system version filter.",
)
@click.option(
    "--python-version",
    "-p",
    type=str,
    default=None,
    metavar="PY_VERSION",
    help="Python interpreter version filter.",
)
@click.option(
    "--cuda-version",
    type=str,
    default=None,
    metavar="CUDA_VERSION",
    help="CUDA version filter.",
)
@click.option(
    "--image-name",
    type=str,
    default=None,
    metavar="IMAGE_NAME",
    help="Filter based on image name.",
)
@click.option(
    "--library-name",
    type=str,
    default=None,
    metavar="LIBRARY_NAME",
    help="Filter based on library name.",
)
@click.option(
    "--symbol",
    type=str,
    default=None,
    metavar="SYMBOL",
    help="Filter based on symbol.",
)
@click.option(
    "--package-name",
    type=str,
    default=None,
    metavar="PACKAGE_NAME",
    help="Filter based on Python package name.",
)
@click.option(
    "--rpm-package-name",
    type=str,
    default=None,
    metavar="RPM_PACKAGE_NAME",
    help="Filter based on RPM package name.",
)
@handle_cli_exception
def images(
    output_format: Optional[str],
    os_name: Optional[str],
    os_version: Optional[str],
    python_version: Optional[str],
    cuda_version: Optional[str],
    image_name: Optional[str],
    library_name: Optional[str],
    symbol: Optional[str],
    package_name: Optional[str],
    rpm_package_name: Optional[str],
) -> None:  # noqa: D412
    """Check available Thoth container images.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos images --output-format json

      thamos images --os-name fedora --os-version 35 --python-version 3.9

      thamos images --symbol GLIBC_FOO
    [/purple]
    """
    result = list_thoth_container_images(
        os_name=os_name,
        os_version=os_version,
        python_version=python_version,
        cuda_version=cuda_version,
        image_name=image_name,
        library_name=library_name,
        symbol=symbol,
        package_name=package_name,
        rpm_package_name=rpm_package_name,
    )

    if output_format == "yaml":
        yaml.safe_dump({"s2i": result}, sys.stdout)
    elif output_format == "json":
        json.dump({"s2i": result}, sys.stdout, indent=2)
        sys.stdout.write("\n")
    elif output_format == "table":
        for item in result:
            table_content = []
            container_image_search_link = ""
            for key, value in item.items():
                if configuration.thoth_search_ui_url is not None:
                    if key == "package_extract_document_id":
                        container_image_search_link = (
                            f"{configuration.thoth_search_ui_url}image/{value}"
                        )
                key = _REPORT_TRANSLATION_TABLE_IMAGES.get(
                    key, key.replace("_", " ").capitalize()
                )
                key = Text.from_markup(key, style="green bold")
                # Here, key value are ignored. This is a trick to have "table header" as the first column.
                if not value:
                    continue

                table_content.extend([{"key": key, "value": value}])

            if container_image_search_link != "":
                table_content.extend(
                    [
                        {
                            "key": Text.from_markup(
                                "See more details in Thoth Search UI:",
                                style="bold cyan",
                            ),
                            "value": container_image_search_link,
                        }
                    ]
                )
            _print_report(
                table_content,
                title=f"Container image {item.get('environment_name', 'UNKNOWN')}",
                show_header=False,
            )

    sys.exit(1 if any(item.get("type") == "ERROR" for item in result) else 0)


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
        for item in result:
            item.pop("warehouse_api_url", None)
            for key, value in item.items():
                # Substitute booleans as rich does not interpret them.
                if isinstance(value, bool):
                    item[key] = str(value)

        _print_report(
            result,
            title="Python package indexes available for consuming packages",
            translation_table=_REPORT_TRANSLATION_TABLE_INDEXES,
        )

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
) -> None:  # noqa: D412
    """Add one or multiple requirements to the project.

    Add one or multiple requirements to the direct dependency listing without actually installing them.
    The supplied requirement is specified using PEP-508 standard.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos add flask

      thamos add tensorflow --runtime-environment training

      thamos add --dev 'pytest~=6.2.0'

      thamos add 'importlib-metadata; python_version < "3.8"'
    [/purple]
    """
    add_requirements_to_project(
        requirement=requirement,
        runtime_environment=runtime_environment,
        index_url=index_url,
        dev=dev,
    )


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
) -> None:  # noqa: D412
    """Remove the given requirement.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos remove flask

      thamos remove pytest --runtime-environment training
    [/purple]
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


@cli.command("support", short_help="Collect environment and configuration information.")
@click.option(
    "--output",
    "-o",
    metavar="FILE",
    type=str,
    help="Specify output file",
    default="-",
)
def support(output: str) -> None:
    """Collect information from the current environment to report an issue."""
    info = collect_support_information_dict()

    if output == "-":
        json.dump(info, sys.stdout, sort_keys=True, indent=2)
    else:
        with open(output, "w") as output_file:
            json.dump(info, output_file, sort_keys=True, indent=2)


@cli.command("whatprovides", short_help="Check packages providing the given import.")
@click.pass_context
@click.option(
    "--output-format",
    "-o",
    type=click.Choice(["json", "yaml", "table"]),
    default="table",
    help="Specify output format for the status report.",
)
@click.argument("import_name", type=str, required=True)
@handle_cli_exception
def whatprovides(import_name: str, output_format: str) -> None:  # noqa: D412
    """For a given import returns list of packages with matching modules.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos whatprovides sklearn

      thamos whatprovides 'sklearn.linear_model.*'
    [/purple]
    """
    _LOGGER.info("Returning information on package %r", import_name)

    result = get_package_from_imported_packages(import_name, raise_on_error=False)
    if not result:
        _LOGGER.error("No package providing %r found", import_name)
        sys.exit(1)

    if output_format == "yaml":
        yaml.safe_dump({"packages": result}, sys.stdout)
    elif output_format == "json":
        json.dump({"packages": result}, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        _print_report(
            result,
            json_output=False,
            title=f"Packages for {import_name}",
            translation_table=_REPORT_TRANSLATION_TABLE_WHATPROVIDES,
        )

    sys.exit(0)


@cli.command("discover", short_help="Discover packages used in the project.")
@click.pass_context
@click.option(
    "--src-path",
    "-s",
    type=str,
    default=".",
    metavar="SRC_PATH",
    envvar="THAMOS_SOURCE_PATH",
    help="Specify path to consider to discover packages.",
)
@click.option(
    "--runtime-environment",
    "-r",
    default=None,
    metavar="NAME",
    envvar="THAMOS_RUNTIME_ENVIRONMENT",
    help="Specify runtime environment to which the given package should be added.",
)
@handle_cli_exception
def discover(
    runtime_environment: typing.Optional[str], src_path: str = "."
) -> None:  # noqa: D412
    """Discover packages used in the project or in a file and add them to requirements.

    If runtime environment is passed, requirements are added to requirements specific
    to the given runtime environment. Otherwise, the default runtime environment is used.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos discover

      thamos discover --runtime-environment production
    [/purple]
    """
    # Obtain list of imports using invectio and verify package from PyPI
    verified_packages = get_verified_packages_from_static_analysis(
        src_path=src_path,
        without_standard_imports=True,
        without_builtin_imports=True,
        without_builtins=True,
        raise_on_error=False,
    )

    # Update requirements files (Pipfile/Pipfile.lock) or requirements.txt (requirements logic)
    for package in verified_packages:
        add_requirements_to_project(
            requirement=[package["package_name"]],
            runtime_environment=runtime_environment,
            index_url=package["index_url"],
            dev=False,
        )


@cli.command("environments")
@click.option(
    "--output-format",
    "-o",
    type=click.Choice(["json", "yaml", "table"]),
    default="table",
    help="Specify output format for the status report.",
)
@click.pass_context
@handle_cli_exception
def environments_(output_format: str) -> None:  # noqa: D412
    """Show available Python environments.

    [bold yellow]Examples:[/bold yellow]
    [purple]

      thamos environments
    [/purple]
    """
    environments = list_python_environments()

    if output_format == "yaml":
        yaml.safe_dump({"environment": environments}, sys.stdout)
    elif output_format == "json":
        json.dump({"environment": environments}, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        _print_report(
            environments,
            json_output=False,
            title="Python environments",
            translation_table=_REPORT_TRANSLATION_TABLE_ENVIRONMENTS,
        )


@cli.command("verify", short_help="Check lock file freshness.")
@click.pass_context
@click.option(
    "--runtime-environment",
    "-r",
    default=None,
    metavar="NAME",
    envvar="THAMOS_RUNTIME_ENVIRONMENT",
    help="Specify runtime environment from which the given package should be removed.",
)
@handle_cli_exception
def verify(runtime_environment: typing.Optional[str]) -> None:  # noqa: D412
    """Verify the hash in Pipfile.lock is up-to-date in runtime environments configured.

    [bold yellow]Examples:[/bold yellow]
    [purple]

        thamos verify

        thamos verify --runtime-environment training
    [/purple]
    """
    if configuration.requirements_format != "pipenv":
        _LOGGER.error(
            "Cannot verify hash of the lock file as the project uses requirements format %r, please switch "
            "to 'pipenv' to have the ability to check the lock file hash",
            configuration.requirements_format,
        )
        sys.exit(2)

    if runtime_environment:
        runtime_environments = [
            configuration.get_runtime_environment(runtime_environment)
        ]
    else:
        runtime_environments = configuration.list_runtime_environments()

    any_error = False
    for runtime_environment_config in runtime_environments:
        runtime_environment_name = runtime_environment_config["name"]

        try:
            project = configuration.get_project(runtime_environment_name)
        except ConfigurationError:
            _LOGGER.error(
                "Failed to obtain configuration for runtime environment %r",
                runtime_environment_name,
            )
            any_error = True
            continue

        if not project.pipfile_lock:
            _LOGGER.error(
                "No lock file found for runtime environment %r",
                runtime_environment_name,
            )
            any_error = True
            continue

        if project.pipfile.hash() != project.pipfile_lock.meta.hash:
            _LOGGER.error("Pipfile.lock is out-of-date. Run `thamos advise` to update.")
            any_error = True
            continue

        _LOGGER.info(
            "Pipfile.lock is up-to-date for runtime environment %r",
            runtime_environment_name,
        )

    sys.exit(any_error is True)


__name__ == "__main__" and cli()
