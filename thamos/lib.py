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

"""Core parts of library for interacting with Thoth."""

import datetime
import logging
import os
import platform
import random
import sys
import typing
from itertools import chain
from time import sleep
from time import monotonic
from contextlib import contextmanager
from functools import partial
from functools import wraps
import pprint
import json
import urllib3
import requests

import yaml
import micropipenv
from termcolor import colored
from invectio import gather_library_usage
from yaspin import yaspin
from yaspin.spinners import Spinners
from thoth.analyzer import run_command
from thoth.python import Project
from thoth.python import Constraints
from thoth.common import ThothAdviserIntegrationEnum
from thoth.common import get_justification_link as jl
from thoth.common import cwd

import thamos.discover
from . import __version__ as thamos_version
from .swagger_client.rest import ApiException
from .swagger_client import ApiClient
from .swagger_client import BuildAnalysisApi
from .swagger_client import Configuration
from .swagger_client import PythonStack
from .swagger_client import AdviseInput
from .swagger_client import ProvenanceInput
from .swagger_client import AdviseApi
from .swagger_client import ImageAnalysisApi
from .swagger_client import ProvenanceApi
from .swagger_client import ContainerImagesApi
from .swagger_client import EnvironmentsApi
from .swagger_client import PythonPackagesApi
from .swagger_client.models import AnalysisResultResponse
from .config import config as thoth_config
from .discover import discover_all
from .exceptions import ApiError
from .exceptions import NoDevRequirements
from .exceptions import NoMatchingPackage
from .exceptions import NoRequirementsFile
from .exceptions import PedanticRunVerificationError
from .exceptions import TimeoutError
from .exceptions import UnknownAnalysisType

from typing import Callable, Any, Union, Dict

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

LAST_ANALYSIS_ID_FILE = ".thoth_last_analysis_id"
_RECOMMENDATION_TYPES_URL = "https://thoth-station.ninja/recommendation-types/"

_LOGGER = logging.getLogger(__name__)
_RETRY_ON_ERROR_COUNT = int(os.getenv("THAMOS_RETRY_ON_ERROR_COUNT", 3))
_RETRY_ON_ERROR_SLEEP = float(os.getenv("THAMOS_RETRY_ON_ERROR_SLEEP", 3.0))
_THAMOS_TIMEOUT = int(os.getenv("THAMOS_TIMEOUT", 2700))
_THAMOS_TOKEN = os.getenv("THAMOS_TOKEN")
_SOURCE = {
    "adviser": "advise/python",
    "provenance-checker": "provenance/python",
    "package-extract": "analyze",
}


def with_api_client(func: typing.Callable):
    """Load configuration entries from Thoth configuration file."""
    # noqa
    @wraps(func)
    def wrapper(*args, **kwargs):
        config = Configuration()
        host = thoth_config.explicit_host
        if not host:
            thoth_config.load_config()
            host = thoth_config.content.get("host") or config.host
        thoth_config.api_discovery(host)
        _LOGGER.debug("Using API: %s", thoth_config.api_url)
        config.host = thoth_config.api_url
        config.verify_ssl = thoth_config.tls_verify

        start = monotonic()
        api_client = ApiClient(configuration=config)
        # Override default user-agent.
        api_client.user_agent = (
            f"Thamos/{thamos_version} (Python {platform.python_version()}; "
            f"{platform.system()} {platform.release()})"
        )
        result = func(api_client, *args, **kwargs)
        _LOGGER.debug("Elapsed seconds processing request: %f", monotonic() - start)
        return result

    return wrapper


def is_analysis_ready(analysis_id: str, *, verify_tls: bool = True) -> bool:
    """Handle the multiple response types available while asking for result of an analysis."""
    config = Configuration()
    host = thoth_config.explicit_host
    if not host:
        thoth_config.load_config()
        host = thoth_config.content.get("host") or config.host
    source = analysis_id.rsplit("-", maxsplit=2)[0]
    source_url = _SOURCE.get(source)
    response = requests.get(
        f"https://{host}/api/v1/{source_url}/{analysis_id}", verify=verify_tls
    )
    if response.status_code == 202:
        return False
    elif response.status_code in (200, 400):
        # Return true if result is ready.
        return True

    raise ApiError(
        f"Thoth Backend didn't respond with correct status code. Returned code - "
        f"{response.status_code}: {response.text}"
    )


def _get_spinner() -> object:
    """Choose the spinner, wisely."""
    today = datetime.datetime.now()
    if today.month == 12 and today.day in (24, 25, 26):  # Christmas.
        return Spinners.christmas
    if (today.month == 1 and today.day == 1) or (
        today.month == 12 and today.day == 31
    ):  # End or start of the year.
        return Spinners.earth
    if today.month == 2 and today.day == 14:  # Valentine's day.
        return Spinners.hearts
    if today.month == 4 and today.day == 1:  # Fool's day.
        return Spinners.smiley
    if today.month == 4 and today.day == 17:  # Easter.
        return Spinners.orangeBluePulse
    if today.month == 10 and today.day == 31:  # Halloween.
        return Spinners.monkey
    if today.hour == 7:  # A morning run.
        return Spinners.runner
    if today.hour >= 22:  # Isn't it too late?
        return Spinners.moon

    return Spinners.clock if random.random() > 0.1 else Spinners.mindblown


def _wait_for_analysis(
    status_func: Callable[..., Any],
    analysis_id: str,
    *,
    timeout: typing.Optional[int] = None,
    verify_tls: bool = True,
) -> None:
    """Wait for ongoing analysis to finish."""
    # noqa
    @contextmanager
    def _no_spinner():
        yield

    spinner = partial(
        yaspin,
        _get_spinner(),
        text=f"Waiting for response from Thoth (analysis: {analysis_id})...",
    )  # type: Union[Callable[..., Any], partial[Any]]
    if _LOGGER.getEffectiveLevel() == logging.DEBUG or bool(
        int(os.getenv("THAMOS_NO_PROGRESSBAR", 1))
    ):
        # CLI automatically injects THAMOS_NO_PROGRESSBAR=0 if user did not turned it off explictily.
        spinner = _no_spinner

    sleep_time = 0.5
    retries = 0
    timeout = timeout if timeout is not None else _THAMOS_TIMEOUT
    with spinner():
        start_time = monotonic()
        while True:
            if timeout and monotonic() - start_time > timeout:
                raise TimeoutError(
                    f"Thoth backend did not respond in time, timeout set "
                    f"to {timeout} - see {jl('thamos_timeout')}"
                )

            try:
                response = status_func(analysis_id, verify_tls=verify_tls)
            except Exception as exc:
                if retries >= _RETRY_ON_ERROR_COUNT:
                    raise

                retries += 1
                _LOGGER.error("Failed to obtain status from Thoth: %s", str(exc))
                _LOGGER.warning(
                    "Retrying in a few moments... (attempt %d/%d)",
                    retries,
                    _RETRY_ON_ERROR_COUNT,
                )
                sleep(_RETRY_ON_ERROR_SLEEP)
                continue

            retries = 0  # Reset counter as we obtained a valid response.
            if response:
                break

            if _LOGGER.getEffectiveLevel() <= logging.DEBUG:
                _LOGGER.debug(
                    "Waiting for %r to finish for %g seconds (state: %s)",
                    analysis_id,
                    sleep_time,
                    (get_status(analysis_id) or {}).get("state", "N/A"),
                )

            sleep(sleep_time)
            sleep_time = min(sleep_time * 2, 8)


def _note_last_analysis_id(analysis_id: str) -> None:
    """Store analysis id in a temporary file to keep analysis id for thamos log optional."""
    if int(os.getenv("THAMOS_DISABLE_LAST_ANALYSIS_ID_FILE", 0)):
        _LOGGER.debug("Last analysis id will not be noted")
        return

    _LOGGER.debug("Noting last analysis id %r", analysis_id)
    try:
        with open(LAST_ANALYSIS_ID_FILE, "w") as analysis_id_file:
            analysis_id_file.write(analysis_id)
    except Exception as exc:
        _LOGGER.warning("Failed to write analysis id to a temporary file: %s", str(exc))


def get_last_analysis_id() -> str:
    """Retrieve last analysis id from a temporary file."""
    try:
        with open(LAST_ANALYSIS_ID_FILE, "r") as analysis_id_file:
            analysis_id = analysis_id_file.readline().strip()
    except Exception as exc:
        raise FileNotFoundError(
            "Cannot retrieve last analysis id, you need to provide analysis id explicitly"
        ) from exc

    return analysis_id


def _retrieve_analysis_result(
    retrieve_func: Callable[..., Any], analysis_id: str
) -> Any:
    """Retrieve analysis result, raise error if analysis failed."""
    retries = 0
    while True:
        try:
            return retrieve_func(analysis_id)
        except ApiException as exc:
            if exc.status == 400:
                # Re-raise if the exception is bad request (e.g. analysis did not finish successfully).
                raise

            _LOGGER.debug(
                "Retrieved error response %s from server: %s", exc.status, exc.reason
            )
            response = json.loads(exc.body)

            if "error" in response:
                # Error produced based on API endpoints semantics...
                _LOGGER.debug("Error from Thoth: %s", response)
                _LOGGER.error("%s (analysis: %s)", response["error"], analysis_id)
            else:
                # Other errors (e.g. internal server error).
                _LOGGER.error("Error from Thoth: %s", response)

            if retries >= _RETRY_ON_ERROR_COUNT:
                return None

            retries += 1
            _LOGGER.warning(
                "Retrying in a few moments... (attempt %d/%d)",
                retries,
                _RETRY_ON_ERROR_COUNT,
            )
            sleep(_RETRY_ON_ERROR_SLEEP)


def get_static_analysis(
    src_path: str = ".",
    *,
    without_standard_imports: bool = False,
    without_builtin_imports: bool = False,
    without_builtins: bool = False,
) -> typing.Optional[dict]:
    """Get static analysis of files used in project."""
    # We are running in the root directory of project, use the root part for gathering static analysis.
    _LOGGER.info("Performing static analysis of sources to gather library usage")
    try:
        library_usage = gather_library_usage(
            src_path,
            ignore_errors=True,
            without_standard_imports=without_standard_imports,
            without_builtin_imports=without_builtin_imports,
            without_builtins=without_builtins,
        )
    except FileNotFoundError:
        _LOGGER.warning("No library usage was aggregated - no Python sources found")
        return None

    report = {}  # type: Dict[Any, Any]
    for file_record in library_usage["report"].values():
        for library, usage in file_record.items():
            # We could filter out some of the libraries which were used.
            if library not in report:
                report[library] = set()

            report[library].update(usage)

    return {
        "report": {k: list(v) for k, v in report.items()},
        "version": library_usage["version"],
    }


def _is_s2i() -> bool:
    """Check if we run in an OpenShift s2i build."""
    # This environment variable is used by OpenShift's s2i build process.
    return "STI_SCRIPTS_PATH" in os.environ


def _get_origin() -> typing.Optional[str]:
    """Check git origin configured."""
    result = run_command("git config --get remote.origin.url", raise_on_error=False)
    if result.return_code != 0:
        _LOGGER.debug(
            "Failed to obtain information about git origin: %s", result.stderr
        )
        return None

    origin = result.stdout.strip()
    if origin:
        _LOGGER.debug("Found git origin %r", origin)
        return origin

    return None


def advise_using_config(
    pipfile: str,
    pipfile_lock: str,
    config: str,
    *,
    runtime_environment_name: typing.Optional[str] = None,
    constraints: typing.Optional[str] = None,
    src_path: str = ".",
    recommendation_type: str = None,
    dev: bool = False,
    no_static_analysis: bool = False,
    no_user_stack: bool = False,
    nowait: bool = False,
    force: bool = False,
    debug: bool = False,
    origin: typing.Optional[str] = None,
    timeout: typing.Optional[int] = None,
    github_event_type: typing.Optional[str] = None,
    github_check_run_id: typing.Optional[int] = None,
    github_installation_id: typing.Optional[int] = None,
    github_base_repo_url: typing.Optional[str] = None,
    source_type: typing.Optional[ThothAdviserIntegrationEnum] = None,
    labels: typing.Optional[Dict[str, str]] = None,
) -> typing.Optional[typing.Tuple[typing.Dict[str, typing.Any], bool]]:
    """Trigger advise, respecting the configuration file supplied directly as a string or as a file path."""
    try:
        thoth_config.load_config_from_file(config)
    except (FileNotFoundError, IOError):
        thoth_config.load_config_from_string(config)

    return advise(
        pipfile=pipfile,
        pipfile_lock=pipfile_lock,
        constraints=constraints,
        recommendation_type=recommendation_type,
        src_path=src_path,
        runtime_environment=thoth_config.get_runtime_environment(
            runtime_environment_name
        ),
        runtime_environment_name=runtime_environment_name,
        dev=dev,
        no_static_analysis=no_static_analysis,
        no_user_stack=no_user_stack,
        nowait=nowait,
        force=force,
        debug=debug,
        origin=origin,
        timeout=timeout,
        github_event_type=github_event_type,
        github_check_run_id=github_check_run_id,
        github_installation_id=github_installation_id,
        github_base_repo_url=github_base_repo_url,
        source_type=source_type,
        verify_tls=thoth_config.tls_verify,
        labels=labels,
    )


@with_api_client
def advise(
    api_client: ApiClient,
    pipfile: str,
    pipfile_lock: str,
    *,
    constraints: typing.Optional[str] = None,
    recommendation_type: typing.Optional[str] = None,
    runtime_environment: typing.Optional[dict] = None,
    src_path: str = ".",
    runtime_environment_name: typing.Optional[str] = None,
    dev: bool = False,
    no_static_analysis: bool = False,
    no_user_stack: bool = False,
    nowait: bool = False,
    force: bool = False,
    debug: bool = False,
    origin: typing.Optional[str] = None,
    timeout: typing.Optional[int] = None,
    github_event_type: typing.Optional[str] = None,
    github_check_run_id: typing.Optional[int] = None,
    github_installation_id: typing.Optional[int] = None,
    github_base_repo_url: typing.Optional[str] = None,
    source_type: typing.Optional[ThothAdviserIntegrationEnum] = None,
    justification: typing.Optional[Dict] = None,
    stack_info: typing.Optional[Dict] = None,
    kebechet_metadata: typing.Optional[Dict] = None,
    verify_tls: bool = True,
    labels: typing.Optional[Dict[str, str]] = None,
) -> typing.Optional[tuple]:
    """Submit a stack for adviser checks and wait for results."""
    if not pipfile:
        raise ValueError("No Pipfile content provided for advises")

    if runtime_environment is None:
        runtime_environment = thoth_config.get_runtime_environment(
            runtime_environment_name
        )

    if runtime_environment_name is None and runtime_environment:
        runtime_environment_name = runtime_environment.get("name")

    if (runtime_environment and runtime_environment_name) and runtime_environment.get(
        "name"
    ) != runtime_environment_name:
        raise ValueError(
            "Runtime environment name supplied does not match with the one stated in the config file"
        )

    if recommendation_type is None:
        priority = (
            runtime_environment.pop("recommendation_type", None),
            thoth_config.content.get("recommendation_type", None),
            "stable",
        )
        recommendation_type = next(filter(bool, priority))

    _LOGGER.info(
        "Using %r recommendation type - see %s",
        recommendation_type,
        _RECOMMENDATION_TYPES_URL,
    )

    if no_user_stack and pipfile_lock:
        _LOGGER.warning(
            "The user stack found in the lock file will not be supplied as requested"
        )
        pipfile_lock = ""

    library_usage = None
    if not no_static_analysis:
        library_usage = get_static_analysis(src_path)
        _LOGGER.debug(
            "Library usage:%s",
            "\n" + json.dumps(library_usage, indent=2) if library_usage else None,
        )

    stack = PythonStack(requirements=pipfile, requirements_lock=pipfile_lock or "")

    if runtime_environment:
        # Override recommendation type specified explicitly in the runtime environment entry.
        runtime_environment.pop("recommendation_type", None)

    input_args: Dict[str, Any] = {
        "application_stack": stack,
        "runtime_environment": runtime_environment,
        "library_usage": library_usage,
    }

    if kebechet_metadata:
        input_args["kebechet_metadata"] = kebechet_metadata
    if justification:
        input_args["justification"] = justification
    if stack_info:
        input_args["stack_info"] = stack_info
    if constraints:
        input_args["constraints"] = constraints
    if labels:
        input_args["labels"] = labels
    elif runtime_environment.get("labels"):
        input_args["labels"] = runtime_environment["labels"]

    advise_input = AdviseInput(**input_args)
    api_instance = AdviseApi(api_client)

    if recommendation_type:
        recommendation_type = recommendation_type.lower()

    if source_type is None and _is_s2i():
        source_type = ThothAdviserIntegrationEnum.S2I

    parameters = {
        "recommendation_type": recommendation_type,
        "debug": debug,
        "force": force,
        "source_type": source_type.name.lower() if source_type is not None else None,
        "origin": _get_origin(),
        "dev": dev,
    }  # type: Dict[str, Any]

    if origin is not None:
        parameters["origin"] = origin

    if github_event_type is not None:
        parameters["github_event_type"] = github_event_type

    if github_check_run_id is not None:
        parameters["github_check_run_id"] = github_check_run_id

    if github_installation_id is not None:
        parameters["github_installation_id"] = github_installation_id

    if github_base_repo_url is not None:
        parameters["github_base_repo_url"] = github_base_repo_url

    if _THAMOS_TOKEN:
        parameters["token"] = _THAMOS_TOKEN

    response = api_instance.post_advise_python(advise_input, **parameters)

    _LOGGER.info(
        "Successfully submitted advise analysis %r to %r",
        response.analysis_id,
        thoth_config.api_url,
    )

    _note_last_analysis_id(response.analysis_id)

    _LOGGER.debug("Analysis parameters:\n%r", pprint.pformat(parameters))
    _LOGGER.debug("Adviser input:\n%s", advise_input.to_str())

    if nowait:
        return response.analysis_id
    # We call custom status function for advise until swagger client supports mulitple response codes.
    _wait_for_analysis(
        is_analysis_ready, response.analysis_id, timeout=timeout, verify_tls=verify_tls
    )
    _LOGGER.debug("Retrieving adviser result for %r", response.analysis_id)
    response = _retrieve_analysis_result(
        api_instance.get_advise_python, response.analysis_id
    )
    if not response:
        return None

    _LOGGER.debug("Adviser check metadata: %r", response.metadata)
    return response.result.to_dict(), response.result.error


def advise_here(
    recommendation_type: typing.Optional[str] = None,
    *,
    runtime_environment: typing.Optional[dict] = None,
    src_path: str = ".",
    runtime_environment_name: typing.Optional[str] = None,
    dev: bool = False,
    no_static_analysis: bool = False,
    no_user_stack: bool = False,
    nowait: bool = False,
    force: bool = False,
    debug: bool = False,
    timeout: typing.Optional[int] = None,
    origin: typing.Optional[str] = None,
    github_event_type: typing.Optional[str] = None,
    github_check_run_id: typing.Optional[int] = None,
    github_installation_id: typing.Optional[int] = None,
    github_base_repo_url: typing.Optional[str] = None,
    source_type: typing.Optional[ThothAdviserIntegrationEnum] = None,
    justification: typing.Optional[Dict] = None,
    stack_info: typing.Optional[Dict] = None,
    kebechet_metadata: typing.Optional[Dict] = None,
    verify_tls: bool = True,
    labels: typing.Optional[Dict[str, str]] = None,
) -> typing.Optional[tuple]:
    """Run advise in current directory, requires no arguments."""
    if runtime_environment_name is not None and runtime_environment is not None:
        raise ValueError(
            "Both runtime_environment and runtime_environment_name were set."
        )

    if runtime_environment is None and runtime_environment_name is None:
        runtime_environment = thoth_config.get_runtime_environment()

    if runtime_environment:
        runtime_environment_name = runtime_environment["name"]

    # get_overlays_directory() returns the current working directory if overlays_dir is not configured so this change
    # should not result in a behavioral change
    overlay_dir = thoth_config.get_overlays_directory(
        runtime_environment_name=runtime_environment_name
    )

    with cwd(overlay_dir):
        requirements_format = thoth_config.requirements_format
        if requirements_format == "pipenv":
            _LOGGER.info(
                "Using Pipenv files to manage dependencies located in %r", os.getcwd()
            )
            pipfile_lock_exists = os.path.exists("Pipfile.lock")

            if pipfile_lock_exists:
                _LOGGER.info(
                    "Submitting Pipfile.lock as a base for user's stack scoring - see %s",
                    jl("user_stack"),
                )

            project = Project.from_files(
                pipfile_path="Pipfile",
                pipfile_lock_path="Pipfile.lock",
                without_pipfile_lock=not os.path.exists("Pipfile.lock"),
            )

            if (
                pipfile_lock_exists
                and project.pipfile_lock.meta.hash["sha256"]
                != project.pipfile.hash()["sha256"]
            ):
                _LOGGER.error(
                    "Pipfile hash stated in Pipfile.lock %r does not correspond to Pipfile hash %r - was Pipfile "
                    "adjusted? This error is not critical.",
                    project.pipfile_lock.meta.hash["sha256"][:6],
                    project.pipfile.hash()["sha256"][:6],
                )
        elif requirements_format in ("pip", "pip-tools", "pip-compile"):
            _LOGGER.info(
                "Using requirements.txt file to manage dependencies located in %r",
                os.getcwd(),
            )
            project = Project.from_pip_compile_files(allow_without_lock=True)
        else:
            raise ValueError(
                f"Unknown configuration option for requirements format: {requirements_format!r}"
            )

        constraints_str = None
        if os.path.exists("constraints.txt"):
            _LOGGER.info("Using constraints.txt file located in %r", os.getcwd())
            with open("constraints.txt") as constraints_file:
                constraints_str = constraints_file.read()

            # Try to load constraints before the request to verify their correctness without sending request to the
            # backend.
            Constraints.from_string(constraints_str)

        pipfile = project.pipfile.to_string()
        pipfile_lock_str = (
            project.pipfile_lock.to_string() if project.pipfile_lock else ""
        )

        return advise(
            pipfile=pipfile,
            pipfile_lock=pipfile_lock_str,
            constraints=constraints_str,
            recommendation_type=recommendation_type,
            src_path=src_path,
            runtime_environment=runtime_environment,
            runtime_environment_name=runtime_environment_name,
            dev=dev,
            no_static_analysis=no_static_analysis,
            no_user_stack=no_user_stack,
            nowait=nowait,
            force=force,
            debug=debug,
            origin=origin,
            timeout=timeout,
            source_type=source_type,
            github_event_type=github_event_type,
            github_check_run_id=github_check_run_id,
            github_installation_id=github_installation_id,
            github_base_repo_url=github_base_repo_url,
            justification=justification,
            stack_info=stack_info,
            kebechet_metadata=kebechet_metadata,
            verify_tls=verify_tls,
            labels=labels,
        )


@with_api_client
def provenance_check(
    api_client: ApiClient,
    pipfile: str,
    pipfile_lock: str,
    *,
    nowait: bool = False,
    force: bool = False,
    debug: bool = False,
    origin: typing.Optional[str] = None,
    timeout: typing.Optional[int] = None,
    justification: typing.Optional[Dict[str, Any]] = None,
    stack_info: typing.Optional[Dict[str, Any]] = None,
    kebechet_metadata: typing.Optional[Dict[str, Any]] = None,
    verify_tls: bool = False,
) -> typing.Optional[tuple]:
    """Submit a stack for provenance checks and wait for results."""
    if not pipfile:
        raise ValueError("No Pipfile content provided for provenance checks")

    input_args: Dict[str, Any] = {
        "application_stack": PythonStack(
            requirements=pipfile, requirements_lock=pipfile_lock
        ),
    }
    if justification:
        input_args["justification"] = justification
    if stack_info:
        input_args["stack_info"] = stack_info
    if kebechet_metadata:
        input_args["kebechet_metadata"] = kebechet_metadata

    provenance_input = ProvenanceInput(**input_args)

    provenance_kwargs: Dict[str, Any] = {
        "debug": debug,
        "force": force,
    }
    if origin:
        provenance_kwargs["origin"] = origin
    if _THAMOS_TOKEN:
        provenance_kwargs["token"] = _THAMOS_TOKEN

    api_instance = ProvenanceApi(api_client)
    response = api_instance.post_provenance_python(
        provenance_input, **provenance_kwargs
    )
    _LOGGER.info(
        "Successfully submitted provenance check analysis %r to %r",
        response.analysis_id,
        thoth_config.api_url,
    )

    _note_last_analysis_id(response.analysis_id)

    if nowait:
        return response.analysis_id

    _wait_for_analysis(
        is_analysis_ready, response.analysis_id, timeout=timeout, verify_tls=verify_tls
    )
    _LOGGER.debug("Retrieving provenance check result for %r", response.analysis_id)
    response = _retrieve_analysis_result(
        api_instance.get_provenance_python, response.analysis_id
    )
    if not response:
        return None

    _LOGGER.debug("Provenance check metadata: %r", response.metadata)
    result = response.result.to_dict()
    return result["report"], result["error"]


def provenance_check_here(
    *,
    nowait: bool = False,
    force: bool = False,
    debug: bool = False,
    origin: typing.Optional[str] = None,
    timeout: typing.Optional[int] = None,
    justification: typing.Optional[Dict[str, Any]] = None,
    stack_info: typing.Optional[Dict[str, Any]] = None,
    kebechet_metadata: typing.Optional[Dict[str, Any]] = None,
    verify_tls: bool = True,
) -> typing.Optional[tuple]:
    """Submit a provenance check in current directory."""
    if not os.path.isfile("Pipfile"):
        raise FileNotFoundError("No Pipfile found in current directory")

    if not os.path.isfile("Pipfile.lock"):
        raise FileNotFoundError("No Pipfile.lock found in current directory")

    with open("Pipfile", "r") as pipfile, open("Pipfile.lock", "r") as piplock:
        return provenance_check(
            pipfile.read(),
            piplock.read(),
            nowait=nowait,
            force=force,
            debug=debug,
            origin=origin,
            timeout=timeout,
            justification=justification,
            stack_info=stack_info,
            kebechet_metadata=kebechet_metadata,
            verify_tls=verify_tls,
        )


@with_api_client
def image_analysis(
    api_client: ApiClient,
    image: str,
    *,
    environment_type: str,
    registry_user: str = None,
    registry_password: str = None,
    verify_tls: bool = True,
    nowait: bool = False,
    force: bool = False,
    timeout: typing.Optional[int] = None,
    debug: bool = False,
) -> Union[Dict, str, None]:
    """Submit an image for analysis to Thoth."""
    if not image:
        raise ValueError("No image provided")

    api_instance = ImageAnalysisApi(api_client)
    if registry_user or registry_password:
        # Swagger client handles None in a different way - we need to explicitly avoid passing
        # registry user and registry password if they are not set.
        response = api_instance.post_analyze(
            image=image,
            debug=debug,
            registry_user=registry_user,
            registry_password=registry_password,
            verify_tls=verify_tls,
            force=force,
            environment_type=environment_type,
        )
    else:
        response = api_instance.post_analyze(
            image=image, debug=debug, verify_tls=verify_tls, force=force
        )

    _LOGGER.info(
        "Successfully submitted provenance check analysis %r to %r",
        response.analysis_id,
        thoth_config.api_url,
    )
    if nowait:
        return response.analysis_id

    _wait_for_analysis(
        is_analysis_ready, response.analysis_id, timeout=timeout, verify_tls=verify_tls
    )
    _LOGGER.debug(
        "Retrieving image analysis result result for %r", response.analysis_id
    )
    response = _retrieve_analysis_result(api_instance.get_analyze, response.analysis_id)
    if not response:
        return None

    _LOGGER.debug("Image analysis metadata: %r", response.metadata)
    return response.result


@with_api_client
def build_analysis(
    api_client: ApiClient,
    build_log: dict,
    base_image: str,
    output_image: str,
    *,
    environment_type: str,
    base_registry_user: typing.Optional[str] = None,
    base_registry_password: typing.Optional[str] = None,
    base_registry_verify_tls: bool = True,
    output_registry_user: typing.Optional[str] = None,
    output_registry_password: typing.Optional[str] = None,
    output_registry_verify_tls: bool = True,
    origin: typing.Optional[str] = None,
    nowait: bool = False,
    force: bool = False,
    debug: bool = False,
) -> typing.Union[typing.Dict, str]:
    """Submit a build image and logs for analysis to Thoth."""
    if build_log or base_image or output_image:
        build_detail = {
            "build_log": build_log,
            "base_image": base_image,
            "output_image": output_image,
        }
    else:
        raise ValueError("No build info provided")

    params = dict(
        body=build_detail,
        base_registry_user=base_registry_user,
        base_registry_password=base_registry_password,
        base_registry_verify_tls=base_registry_verify_tls,
        output_registry_user=output_registry_user,
        output_registry_password=output_registry_password,
        output_registry_verify_tls=output_registry_verify_tls,
        environment_type=environment_type,
        origin=origin,
        debug=debug,
        force=force,
    )

    # Swagger client handles None in a different way - we need to explicitly avoid passing
    # values that are not present.
    params = {k: v for k, v in params.items() if v is not None}

    api_instance = BuildAnalysisApi(api_client)
    response = api_instance.post_build(**params)

    _LOGGER.info("Successfully submitted build analysis to %r", thoth_config.api_url)
    _LOGGER.debug("Build analysis parameters: %r", params)
    if nowait:
        return response

    return response


@with_api_client
def get_log(api_client: ApiClient, analysis_id: str = None):
    """Get log of an analysis - the analysis type and endpoint are automatically derived from analysis id.

    If analysis_id is not provided, its get from the last thamos call which stores it in a temporary file.
    """
    if not analysis_id:
        analysis_id = get_last_analysis_id()

    if analysis_id.startswith("package-extract-"):
        api_instance = ImageAnalysisApi(
            api_client
        )  # type: Union[ImageAnalysisApi, ProvenanceApi, AdviseApi]
        method = api_instance.get_analyze_log  # type: ignore
    elif analysis_id.startswith("provenance-checker-"):
        api_instance = ProvenanceApi(api_client)
        method = api_instance.get_provenance_python_log  # type: ignore
    elif analysis_id.startswith("adviser-"):
        api_instance = AdviseApi(api_client)
        method = api_instance.get_advise_python_log  # type: ignore
    else:
        raise UnknownAnalysisType(
            "Cannot determine analysis type from identifier: %r", analysis_id
        )

    json_log = method(analysis_id).log

    if not json_log:
        return json_log

    result = ""
    for line in json_log.splitlines():
        try:
            content = json.loads(line)
            if not int(os.getenv("THAMOS_NO_EMOJI", 0)):
                if content["levelname"] == "DEBUG":
                    message = colored(content["message"], "green")
                elif content["levelname"] == "INFO":
                    message = colored(content["message"], "cyan")
                elif content["levelname"] == "WARNING":
                    message = colored(content["message"], "yellow", attrs=["bold"])
                elif content["levelname"] in ("ERROR", "CRITICAL"):
                    message = colored(content["message"], "red", attrs=["bold"])
                else:
                    message = content["message"]

                result += "{} {:<27} {}: {}\n".format(
                    content["asctime"], content["name"], content["levelname"], message
                )
            else:
                result += "{} {:<27} {}: {}\n".format(
                    content["asctime"],
                    content["name"],
                    content["levelname"],
                    content["message"],
                )
        except Exception:
            # If the content parsed does not carry logger information or has not relevant
            # entries, log the original message.
            result += line + "\n"
            continue

    return result


@with_api_client
def get_status(api_client: ApiClient, analysis_id: typing.Optional[str] = None):
    """Get status of an analysis - the analysis type and endpoint are automatically derived from analysis id.

    If analysis_id is not provided, its get from the last thamos call which stores it in a temporary file.
    """
    if not analysis_id:
        analysis_id = get_last_analysis_id()

    if analysis_id.startswith("package-extract-"):
        api_instance = ImageAnalysisApi(
            api_client
        )  # type: Union[ImageAnalysisApi, ProvenanceApi, AdviseApi]
        method = api_instance.get_analyze_status  # type: ignore
    elif analysis_id.startswith("provenance-checker-"):
        api_instance = ProvenanceApi(api_client)
        method = api_instance.get_provenance_python_status  # type: ignore
    elif analysis_id.startswith("adviser-"):
        api_instance = AdviseApi(api_client)
        method = api_instance.get_advise_python_status  # type: ignore
    else:
        raise UnknownAnalysisType(
            "Cannot determine analysis type from identifier: %r", analysis_id
        )

    return method(analysis_id).status.to_dict()


@with_api_client
def get_analysis_results(
    api_client: ApiClient, analysis_id: typing.Optional[str] = None
):
    """Get the analysis result from a given id."""
    if not analysis_id:
        analysis_id = get_last_analysis_id()

    if analysis_id.startswith("package-extract-"):
        api_instance = ImageAnalysisApi(
            api_client
        )  # type: Union[ImageAnalysisApi, ProvenanceApi, AdviseApi]
        method = api_instance.get_analyze  # type: ignore
        response = _retrieve_analysis_result(
            method, analysis_id
        )  # type: AnalysisResultResponse
        return response.result
    elif analysis_id.startswith("provenance-checker-"):
        api_instance = ProvenanceApi(api_client)
        method = api_instance.get_provenance_python  # type: ignore
        response = _retrieve_analysis_result(method, analysis_id)
        return response.result["report"], response.result["error"]
    elif analysis_id.startswith("adviser-"):
        api_instance = AdviseApi(api_client)
        method = api_instance.get_advise_python  # type: ignore
        response = _retrieve_analysis_result(method, analysis_id)
        return response.result.to_dict(), response.result.error
    else:
        raise UnknownAnalysisType(
            "Cannot determine analysis type from identifier: %r", analysis_id
        )


def install_using_config(
    config: str,
    runtime_environment_name: typing.Optional[str] = None,
    dev: bool = False,
) -> None:
    """Perform installation given the configuration supplied."""
    try:
        thoth_config.load_config_from_file(config)
    except (FileNotFoundError, IOError):
        thoth_config.load_config_from_string(config)

    install(runtime_environment_name=runtime_environment_name, dev=dev)


def install(
    runtime_environment_name: typing.Optional[str] = None,
    dev: bool = False,
    pip_args: typing.Optional[typing.Tuple[str]] = None,
) -> None:
    """Perform installation of packages for the given runtime environment.

    If the runtime environment is not specified, the first environment stated in the configuration is used.
    """
    method = (
        "pipenv" if thoth_config.requirements_format == "pipenv" else "requirements"
    )

    if not dev and method == "pipenv":
        _LOGGER.warning(
            "Development dependencies will not be installed - see %s", jl("no_dev")
        )

    with cwd(thoth_config.get_overlays_directory(runtime_environment_name)):
        if method == "pipenv":
            if not os.path.isfile("Pipfile.lock"):
                raise NoRequirementsFile(
                    f"No Pipfile.lock found in {os.getcwd()!r} needed to install dependencies, "
                    "issue `thamos advise` resolve dependencies"
                )
            if not os.path.isfile("Pipfile"):  # Required for computing digests.
                raise NoRequirementsFile(
                    f"No Pipfile found in {os.getcwd()!r} needed for the installation process"
                )

            if dev:
                with open("Pipfile.lock") as pipfile_lock_file:
                    content = json.load(pipfile_lock_file)

                if not content.get("develop"):
                    raise NoDevRequirements(
                        "No development requirements found in the lock file, make sure development "
                        "requirements are stated and the resolved stack preserves them by "
                        "using `thamos advise --dev`"
                    )

                del content
        else:
            if not os.path.isfile("requirements.txt"):
                raise NoRequirementsFile(
                    f"No requirements.txt file found in {os.getcwd()!r} needed to install dependencies"
                )

        if runtime_environment_name is None:
            config_entry = thoth_config.get_runtime_environment(
                runtime_environment_name
            )
            runtime_environment_name = config_entry["name"]
        _LOGGER.info(
            "Installing requirements for runtime environment %r",
            runtime_environment_name,
        )

        _LOGGER.info(
            "Using %r installation method to install dependencies stated in %r",
            method,
            os.getcwd(),
        )

        micropipenv_kwargs = {
            "method": method,
            "deploy": True,
            "dev": dev,
            "pip_args": pip_args,
        }

        virtualenv_path = thoth_config.get_virtualenv_path(runtime_environment_name)
        if virtualenv_path:
            if not os.path.isdir(virtualenv_path):
                thoth_config.create_virtualenv()

            micropipenv_kwargs["pip_bin"] = os.path.join(virtualenv_path, "bin", "pip3")

        # micropipenv writes and prints the lockfile which is not very user friendly when thamos is used by a user.
        # Suppress this behavior unless these environment variables options are supplied explicitly.
        old_write = os.getenv("MICROPIPENV_NO_LOCKFILE_WRITE")
        if old_write is None:
            os.environ["MICROPIPENV_NO_LOCKFILE_WRITE"] = "1"

        old_print = os.getenv("MICROPIPENV_NO_LOCKFILE_PRINT")
        if old_print is None:
            os.environ["MICROPIPENV_NO_LOCKFILE_PRINT"] = "1"

        try:
            micropipenv.install(**micropipenv_kwargs)
        finally:
            if old_write is None:
                os.environ.pop("MICROPIPENV_NO_LOCKFILE_WRITE", None)

            if old_print is None:
                os.environ.pop("MICROPIPENV_NO_LOCKFILE_PRINT", None)


@with_api_client
def list_thoth_container_images(
    api_client: ApiClient,
    *,
    os_name: typing.Optional[str] = None,
    os_version: typing.Optional[str] = None,
    python_version: typing.Optional[str] = None,
    cuda_version: typing.Optional[str] = None,
    image_name: typing.Optional[str] = None,
    library_name: typing.Optional[str] = None,
    symbol: typing.Optional[str] = None,
    package_name: typing.Optional[str] = None,
    rpm_package_name: typing.Optional[str] = None,
) -> typing.List[typing.Dict[str, Any]]:
    """Get available Thoth container images."""
    filtering = locals()
    filtering.pop("api_client", None)
    filtering = {k: v for k, v in filtering.items() if v is not None}

    result = []
    page = 0
    while True:
        images = (
            ContainerImagesApi(api_client)
            .list_thoth_container_images(page=page, **filtering)
            .to_dict()["container_images"]
        )
        if not images:
            break
        result.extend(images)
        page += 1

    return result


@with_api_client
def list_python_environments(api_client: ApiClient) -> typing.Dict[str, Any]:
    """Get available Python environments."""
    return (
        EnvironmentsApi(api_client).list_python_environments().to_dict()["environment"]
    )


@with_api_client
def list_python_package_indexes(api_client: ApiClient) -> typing.Dict[str, Any]:
    """Get information about hardware for which Thoth can give recommendations."""
    return (
        PythonPackagesApi(api_client).list_python_package_indexes().to_dict()["indexes"]
    )


@with_api_client
def get_package_from_imported_packages(
    api_client: ApiClient,
    import_name: str,
    raise_on_error: bool = True,
) -> typing.List[Dict[str, Any]]:
    """Get all (package_name, package_version, index_url) triplets for given import package name."""
    try:
        return (
            PythonPackagesApi(api_client)
            .get_package_from_imported_packages(import_name)
            .to_dict()["package_names"]
        )
    except ApiException as exc:
        error_message = f"Failed to obtain package for import {import_name!r} (HTTP status {exc.status})"
        if exc.body:
            try:
                error_message += (
                    f": {str(json.loads(exc.body.decode('utf-8'))['error'])}"
                )
            except json.decoder.JSONDecodeError:
                _LOGGER.error(
                    "Failed to decode backend response (HTTP status %r)", exc.status
                )

        if raise_on_error:
            raise NoMatchingPackage(error_message) from exc

        return []


def get_verified_packages_from_static_analysis(
    src_path: str = ".",
    *,
    without_standard_imports: bool = False,
    without_builtin_imports: bool = False,
    without_builtins: bool = False,
    raise_on_error: bool = True,
) -> typing.List[typing.Dict[str, str]]:
    """Get verified packages from invectio static analysis result."""
    # 1. Obtain list of imports using invectio
    result = get_static_analysis(
        src_path,
        without_standard_imports=without_standard_imports,
        without_builtin_imports=without_builtin_imports,
        without_builtins=without_builtins,
    )

    packages = []
    if result:
        packages = [p for p in result["report"].keys()]

    if not packages:
        _LOGGER.error("No package imports identified in %r", src_path)
        return []

    # 2. For each import verify package (name, version, index) (whatprovides logic)
    verified_packages = []

    for import_name in packages:
        unique_packages: typing.List[typing.Dict] = []

        imported_packages = get_package_from_imported_packages(
            import_name, raise_on_error=raise_on_error
        )
        if not imported_packages:
            _LOGGER.error("No package for import %r found", import_name)
            continue

        for package in imported_packages:
            if package["package_name"] not in [
                p["package_name"] for p in unique_packages
            ]:
                unique_packages.append(
                    {
                        "package_name": package["package_name"],
                        "index_url": package["index_url"],
                    }
                )
            else:
                existing_indexes = [
                    p["index_url"]
                    for p in unique_packages
                    if p["package_name"] == package["package_name"]
                ]

                if package["index_url"] not in existing_indexes:
                    unique_packages.append(
                        {
                            "package_name": package["package_name"],
                            "index_url": package["index_url"],
                        }
                    )

        for unique_package in unique_packages:
            verified_packages.append(unique_package)
            _LOGGER.info(
                "Package name %r identified for import %r",
                unique_package["package_name"],
                import_name,
            )

    return verified_packages


def write_files(
    requirements: typing.Dict[str, Any],
    requirements_lock: typing.Dict[str, Any],
    requirements_format: str,
) -> None:
    """Write content of Pipfile/Pipfile.lock or requirements.in/txt to the current directory."""
    project = Project.from_dict(requirements, requirements_lock)
    if requirements_format == "pipenv":
        _LOGGER.debug("Writing to Pipfile/Pipfile.lock in %r", os.getcwd())
        project.to_files(keep_thoth_section=True)
    elif requirements_format in ("pip", "pip-tools", "pip-compile"):
        _LOGGER.debug("Writing to requirements.in/requirements.txt in %r", os.getcwd())
        project.to_pip_compile_files()
        _LOGGER.debug("No changes to Pipfile to write")
    else:
        raise ValueError(
            f"Unknown requirements format, supported are 'pipenv' and 'pip': {requirements_format!r}"
        )


def load_files(requirements_format: str) -> typing.Tuple[str, typing.Optional[str]]:
    """Load Pipfile/Pipfile.lock or requirements.in/txt from the current directory."""
    if requirements_format == "pipenv":
        _LOGGER.info("Using Pipenv files located in %r directory", os.getcwd())
        pipfile_lock_exists = os.path.exists("Pipfile.lock")

        if pipfile_lock_exists:
            _LOGGER.info(
                "Submitting Pipfile.lock as a base for user's stack scoring - see %s",
                jl("user_stack"),
            )

        project = Project.from_files(
            pipfile_path="Pipfile",
            without_pipfile_lock=not os.path.exists("Pipfile.lock"),
        )

        if (
            pipfile_lock_exists
            and project.pipfile_lock.meta.hash["sha256"]
            != project.pipfile.hash()["sha256"]
        ):
            _LOGGER.error(
                "Pipfile hash stated in Pipfile.lock %r does not correspond to Pipfile hash %r - was Pipfile "
                "adjusted? This error is not critical.",
                project.pipfile_lock.meta.hash["sha256"][:6],
                project.pipfile.hash()["sha256"][:6],
            )
    elif requirements_format in ("pip", "pip-tools", "pip-compile"):
        _LOGGER.info("Using requirements.txt file located in %r directory", os.getcwd())
        project = Project.from_pip_compile_files(allow_without_lock=True)
    else:
        raise ValueError(
            f"Unknown configuration option for requirements format: {requirements_format!r}"
        )
    return (
        project.pipfile.to_string(),
        project.pipfile_lock.to_string() if project.pipfile_lock else None,
    )


def write_configuration(
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


def collect_support_information_dict() -> Dict[str, Any]:
    """Collect environment information suitable to report bugs or issues in a dictionary form."""
    discovery = {}

    for name in dir(thamos.discover):
        if not name.startswith("discover_"):
            continue

        func = getattr(thamos.discover, name)
        discovery[name[len("discover_") :]] = func()

    thoth_config_content = None
    try:
        thoth_config_content = thoth_config.content
    except Exception:
        _LOGGER.exception("Failed to obtain content of Thoth's configuration file")

    thoth_version = None
    try:
        thoth_version = thoth_config.get_thoth_version()
    except Exception:
        _LOGGER.exception("Failed to obtain Thoth version information")

    pip_freeze = None
    try:
        pip_freeze = run_command("pip freeze").stdout.splitlines()
    except Exception:
        _LOGGER.exception("Failed to obtain packages present in the environment")

    last_analysis_id = None
    try:
        last_analysis_id = get_last_analysis_id()
    except FileNotFoundError:
        _LOGGER.warning("Cannot retrieve last analysis identifier")
        pass

    result = {
        "environment": {
            k: v for k, v in os.environ.items() if k.startswith(("THAMOS_", "THOTH_"))
        },
        "is_s2i": _is_s2i(),
        "last_analysis_id": last_analysis_id,
        "thoth_config": thoth_config_content,
        "thoth_version": thoth_version,
        "thamos_version": thamos_version,
        "os_name": os.name,
        "platform_machine": platform.machine(),
        "platform_python_implementation": platform.python_implementation(),
        "platform_release": platform.release(),
        "platform_system": platform.system(),
        "platform_version": platform.version(),
        "python_full_version": platform.python_version(),
        "python_version": ".".join(platform.python_version().split(".")[:2]),
        "sys_platform": sys.platform,
        "pip_freeze": pip_freeze,
        "discovery": discovery,
    }
    return result


def _get_package_entry_str(
    pipfile_lock: Dict[str, Dict[str, typing.Any]], package_name: str
) -> str:
    """Get information about the given package so that they are printed to users."""
    package_entry = pipfile_lock["default"].get(
        package_name, pipfile_lock["develop"].get(package_name)
    )
    if not package_entry:
        # Any error spotted?
        return "UNKNOWN==UNKNOWN from UNKNOWN"

    index_url = "UNKNOWN"
    for source in pipfile_lock["_meta"]["sources"]:
        if package_entry.get("index") == source["name"]:
            index_url = source["url"]
            break

    return f"{package_name}{package_entry.get('version')} from {index_url}"


def _traverse_edges(
    pipfile_lock: Dict[str, Dict[str, str]],
    nodes: typing.List[str],
    edges: typing.List[typing.List[int]],
    seen_nodes: typing.Set[int],
    *,
    starting_node: int,
    indent: int = 2,
    fold: bool = True,
) -> None:
    """Traverse edges of the dependency graph and show its structure to terminal."""
    for edge in edges:
        if edge[0] == starting_node:
            print(
                " " * indent
                + f"↳ {_get_package_entry_str(pipfile_lock, nodes[edge[1]])}"
            )
            if edge[1] not in seen_nodes:
                if fold:
                    seen_nodes.add(edge[1])

                _traverse_edges(
                    pipfile_lock,
                    nodes,
                    edges,
                    seen_nodes=seen_nodes | {edge[1]},
                    starting_node=edge[1],
                    indent=indent + 2,
                    fold=fold,
                )
            else:
                # Note cyclic dependency.
                print(" " * (indent + 2) + "↳ …")


def print_dependency_graph_from_adviser_document(
    adviser_document: typing.Dict[str, typing.Any], *, fold: bool = True
) -> bool:
    """Print dependency graph to stdout from the given document."""
    if not adviser_document["report"]["products"]:
        _LOGGER.error(
            "No dependency graph to show, was the adviser request successful?"
        )
        return False

    if not adviser_document["report"]["products"][0].get("dependency_graph"):
        # XXX: we can remove this check over time.
        _LOGGER.error(
            "No dependency graph to show, was the result computed with recent adviser?"
        )
        return False

    nodes = adviser_document["report"]["products"][0]["dependency_graph"]["nodes"]
    edges = adviser_document["report"]["products"][0]["dependency_graph"]["edges"]

    nodes_idx = {n: i for i, n in enumerate(nodes)}
    # Keep a list of flags stating the given package is a root dependency.
    pipfile = adviser_document["report"]["products"][0]["project"]["requirements"]
    pipfile_lock = adviser_document["report"]["products"][0]["project"][
        "requirements_locked"
    ]

    direct_dependencies = pipfile["packages"].keys()
    if adviser_document["parameters"]["dev"]:
        # Include dev packages in the listing only if dev flag was supplied
        direct_dependencies = chain(direct_dependencies, pipfile["dev-packages"].keys())
    else:
        _LOGGER.warning(
            "Development dependencies will not be shown as no --dev flag was supplied to the resolution process"
        )

    for direct_dependency in direct_dependencies:
        direct_dependency_idx = nodes_idx[direct_dependency]
        print(f"→ {_get_package_entry_str(pipfile_lock, direct_dependency)}")
        _traverse_edges(
            pipfile_lock,
            nodes,
            edges,
            seen_nodes={direct_dependency_idx},
            starting_node=direct_dependency_idx,
            fold=fold,
        )

    return True


def print_dependency_graph(
    analysis_id: typing.Optional[str] = None, *, fold: bool = True
) -> bool:
    """Print dependency graph to stdout produced by the given adviser."""
    analysis_id = analysis_id or get_last_analysis_id()
    if not analysis_id.startswith("adviser-"):
        raise UnknownAnalysisType(
            f"An adviser identifier is required to print a dependency graph, got {analysis_id!r} instead"
        )

    adviser_document, error = get_analysis_results(analysis_id)

    if error:
        print("Cannot print dependency graph as advise was not successful")
        return False

    return print_dependency_graph_from_adviser_document(adviser_document, fold=fold)


def add_requirements_to_project(
    requirement: typing.List[str],
    runtime_environment: typing.Optional[str],
    index_url: str,
    dev: bool,
):
    """Add requirements to project."""
    project = thoth_config.get_project(runtime_environment, missing_dir_ok=True)

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
        runtime_environment_config = thoth_config.get_runtime_environment(
            runtime_environment
        )
        python_version = runtime_environment_config.get("python_version")
        if python_version:
            project.set_python_version(python_version)

    _LOGGER.warning(
        "Changes done might require triggering new advise to resolve dependencies"
    )
    thoth_config.save_project(project)


def check_runtime_environment_run(runtime_environment: Dict[str, Any]) -> None:
    """Check the runtime environment matches runtime environment declared in the config file."""
    discovered = discover_all()

    if runtime_environment.get("base_image") != discovered.get("base_image"):
        raise PedanticRunVerificationError(
            f"Base image configured {runtime_environment.get('base_image')!r} does not match "
            f"base image discovered {discovered.get('base_image')!r}"
        )

    if runtime_environment.get("cuda_version") != discovered.get("cuda_version"):
        raise PedanticRunVerificationError(
            f"CUDA version configured {runtime_environment.get('cuda_version')!r} does not match "
            f"CUDA version discovered {discovered.get('cuda_version')!r}"
        )

    if runtime_environment.get("platform", "linux-x86_64") != discovered.get(
        "platform"
    ):
        raise PedanticRunVerificationError(
            f"Platform configured {runtime_environment.get('platform')!r} does not match "
            f"platform discovered {discovered.get('platform')!r}"
        )

    if runtime_environment.get("python_version") != discovered.get("python_version"):
        raise PedanticRunVerificationError(
            f"Python version configured {runtime_environment.get('python_version')!r} does not match "
            f"Python version discovered {discovered.get('python_version')!r}"
        )

    hw_discovered = discovered.get("hardware") or {}
    hw_configured = runtime_environment.get("hardware") or {}
    if hw_configured.get("cpu_family") is not None and hw_configured.get(
        "cpu_family"
    ) != hw_discovered.get("cpu_family"):
        raise PedanticRunVerificationError(
            f"CPU family configured {hw_configured.get('cpu_family')!r} does not match "
            f"CPU family discovered {hw_discovered.get('cpu_family')!r}"
        )

    if hw_configured.get("cpu_model") is not None and hw_configured.get(
        "cpu_model"
    ) != hw_discovered.get("cpu_model"):
        raise PedanticRunVerificationError(
            f"CPU model configured {hw_configured.get('cpu_model')!r} does not match "
            f"CPU model discovered {hw_discovered.get('cpu_model')!r}"
        )

    if hw_configured.get("gpu_model") is not None and hw_configured.get(
        "gpu_model"
    ) != hw_discovered.get("gpu_model"):
        raise PedanticRunVerificationError(
            f"GPU model configured {hw_configured.get('gpu_model')!r} does not match "
            f"GPU model discovered {hw_discovered.get('gpu_model')!r}"
        )

    os_discovered = discovered.get("operating_system") or {}
    os_configured = runtime_environment.get("operating_system") or {}
    if os_configured.get("name") != os_discovered.get("name"):
        raise PedanticRunVerificationError(
            f"Operating system name configured {os_configured.get('name')!r} does not match "
            f"operating system name discovered {os_discovered.get('name')!r}"
        )

    if os_configured.get("version") != os_discovered.get("version"):
        raise PedanticRunVerificationError(
            f"Operating system version configured {os_configured.get('version')!r} does not match "
            f"operating system version discovered {os_discovered.get('version')!r}"
        )

    _LOGGER.info("Runtime environment configured matches runtime environment used")


def load_dot_env(dot_env_path: str) -> Dict[str, str]:
    """Load .env file and parse its content."""
    if not os.path.isfile(dot_env_path):
        _LOGGER.debug("No .env file at %r found", dot_env_path)
        return {}

    _LOGGER.info("Loading environment variables from %r", dot_env_path)

    env = {}
    with open(dot_env_path) as f:
        for line_no, line in enumerate(f.readlines()):
            line = line.strip()
            if not line or line.startswith("#"):  # Skip comments.
                continue

            parts = line.split("=", maxsplit=1)
            if len(parts) != 2:
                _LOGGER.error(
                    "Failed to parse %r content at line %d, ignoring...",
                    dot_env_path,
                    line_no,
                )
                continue

            env[parts[0]] = parts[1]

    return env
