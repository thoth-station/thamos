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

"""Core parts of library for interacting with Thoth."""

import os
import logging
import typing
import platform
from time import sleep
from time import monotonic
from contextlib import contextmanager
from functools import partial
from functools import wraps
import pprint
import json
import urllib3
import requests

from termcolor import colored
from yaspin import yaspin
from yaspin.spinners import Spinners
from invectio import gather_library_usage
from thoth.analyzer import run_command
from thoth.python import Project
from thoth.common import ThothAdviserIntegrationEnum

from . import __version__ as thamos_version
from .swagger_client.rest import ApiException
from .swagger_client import ApiClient
from .swagger_client import BuildAnalysisApi
from .swagger_client import Configuration
from .swagger_client import PythonStack
from .swagger_client import RuntimeEnvironment
from .swagger_client import AdviseInput
from .swagger_client import AdviseApi
from .swagger_client import ImageAnalysisApi
from .swagger_client import ProvenanceApi
from .swagger_client.models import AnalysisResultResponse
from .config import config as thoth_config
from .exceptions import UnknownAnalysisType
from .exceptions import TimeoutError
from .exceptions import ApiError

from typing import Callable, Any, Union, Dict

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

LAST_ANALYSIS_ID_FILE = ".thoth_last_analysis_id"

_LOGGER = logging.getLogger(__name__)
_RETRY_ON_ERROR_COUNT = int(os.getenv("THAMOS_RETRY_ON_ERROR_COUNT", 3))
_RETRY_ON_ERROR_SLEEP = float(os.getenv("THAMOS_RETRY_ON_ERROR_SLEEP", 3.0))
_THAMOS_TIMEOUT = int(os.getenv("THAMOS_TIMEOUT", 2000))
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


def is_analysis_ready(analysis_id: str) -> bool:
    """Handle the the multiple response types available while asking for result of a anaylsis result."""
    config = Configuration()
    host = thoth_config.explicit_host
    if not host:
        thoth_config.load_config()
        host = thoth_config.content.get("host") or config.host
    source = analysis_id.rsplit("-", 1)[0]
    source_url = _SOURCE.get(source)
    response = requests.get(f"https://{host}/api/v1/{source_url}/{analysis_id}")
    if response.status_code == 202:
        return False
    elif response.status_code in (200, 400):
        # Return true if result is ready.
        return True

    raise ApiError(
        f"Thoth Backend didn't respond with correct status code. Returned code - {response.status_code}"
    )


def _wait_for_analysis(status_func: Callable[..., Any], analysis_id: str) -> None:
    """Wait for ongoing analysis to finish."""
    # noqa
    @contextmanager
    def _no_spinner():
        yield

    spinner = partial(
        yaspin,
        Spinners.clock,
        text=f"Waiting for response from Thoth (analysis: {analysis_id})...",
    )  # type: Union[Callable[..., Any], partial[Any]]
    if _LOGGER.getEffectiveLevel() == logging.DEBUG or bool(
        int(os.getenv("THAMOS_NO_PROGRESSBAR", 1))
    ):
        # CLI automatically injects THAMOS_NO_PROGRESSBAR=0 if user did not turned it off explictily.
        spinner = _no_spinner

    sleep_time = 0.5
    retries = 0
    with spinner():
        start_time = monotonic()
        while True:
            if _THAMOS_TIMEOUT and monotonic() - start_time > _THAMOS_TIMEOUT:
                raise TimeoutError(
                    f"Thoth backend did not respond in time, timeout set to {_THAMOS_TIMEOUT}"
                )
            try:
                response = status_func(analysis_id)
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


def _get_last_analysis_id() -> str:
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


def _get_static_analysis() -> typing.Optional[dict]:
    """Get static analysis of files used in project."""
    # We are running in the root directory of project, use the root part for gathering static analysis.
    _LOGGER.info("Performing static analysis of sources to gather library usage")
    try:
        library_usage = gather_library_usage(
            ".", ignore_errors=True, without_standard_imports=True
        )
    except FileNotFoundError:
        _LOGGER.warning("No library usage was aggregated - no Python sources found")
        return None

    report = {}  # type: Dict[Any, Any]
    for file_record in library_usage["report"].values():
        for library, usage in file_record.items():
            # We could filter out some of the libraries which were used.
            if library not in report:
                report[library] = []

            report[library].extend(usage)

    return {
        "report": report,
        "version": library_usage["version"],
    }


def _is_s2i() -> bool:
    """Check if we run in an OpenShift s2i build."""
    # This environment variable is used by OpenShift's s2i build process.
    return "STI_SCRIPTS_PATH" == os.environ


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


@with_api_client
def advise(
    api_client: ApiClient,
    pipfile: str,
    pipfile_lock: str,
    recommendation_type: str = None,
    *,
    runtime_environment: dict = None,
    runtime_environment_name: str = None,
    dev: bool = False,
    no_static_analysis: bool = False,
    no_user_stack: bool = False,
    nowait: bool = False,
    force: bool = False,
    limit: int = None,
    count: int = 1,
    debug: bool = False,
    origin: str = None,
    github_event_type: typing.Optional[str] = None,
    github_check_run_id: typing.Optional[int] = None,
    github_installation_id: typing.Optional[int] = None,
    github_base_repo_url: typing.Optional[str] = None,
    source_type: typing.Optional[ThothAdviserIntegrationEnum] = None,
) -> typing.Optional[tuple]:
    """Submit a stack for adviser checks and wait for results."""
    if not pipfile:
        raise ValueError("No Pipfile content provided for advises")

    if runtime_environment and runtime_environment_name:
        raise ValueError(
            "Cannot use runtime_environment and runtime_environment_name at the same time"
        )

    if runtime_environment is None:
        runtime_environment = (
            thoth_config.get_runtime_environment(runtime_environment_name) or dict()
        )

    if recommendation_type is None:
        priority = (
            runtime_environment.pop("recommendation_type", None),
            thoth_config.content.get("recommendation_type", None),
            "stable",
        )
        recommendation_type = next(filter(bool, priority))

    if no_user_stack and pipfile_lock:
        _LOGGER.warning(
            "The user stack found in the lock file will not be supplied as requested"
        )
        pipfile_lock = ""

    library_usage = None
    if not no_static_analysis:
        library_usage = _get_static_analysis()
        _LOGGER.debug(
            "Library usage:%s",
            "\n" + json.dumps(library_usage, indent=2) if library_usage else None,
        )

    stack = PythonStack(requirements=pipfile, requirements_lock=pipfile_lock or "")

    if runtime_environment:
        # Override recommendation type specified explicitly in the runtime environment entry.
        runtime_environment.pop("recommendation_type", None)

        runtime_environment = RuntimeEnvironment(**runtime_environment)  # type: ignore

    advise_input = AdviseInput(
        stack, runtime_environment=runtime_environment, library_usage=library_usage
    )
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

    if limit is not None:
        parameters["limit"] = limit

    if count is not None:
        parameters["count"] = count

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
    _wait_for_analysis(is_analysis_ready, response.analysis_id)
    _LOGGER.debug("Retrieving adviser result for %r", response.analysis_id)
    response = _retrieve_analysis_result(
        api_instance.get_advise_python, response.analysis_id
    )
    if not response:
        return None

    _LOGGER.debug("Adviser check metadata: %r", response.metadata)

    return response.result, response.result["error"]


def advise_here(
    recommendation_type: typing.Optional[str] = None,
    *,
    runtime_environment: dict = None,
    runtime_environment_name: typing.Optional[str] = None,
    dev: bool = False,
    no_static_analysis: bool = False,
    no_user_stack: bool = False,
    nowait: bool = False,
    force: bool = False,
    limit: typing.Optional[int] = None,
    count: int = 1,
    debug: bool = False,
    origin: typing.Optional[str] = None,
    github_event_type: typing.Optional[str] = None,
    github_check_run_id: typing.Optional[int] = None,
    github_installation_id: typing.Optional[int] = None,
    github_base_repo_url: typing.Optional[str] = None,
    source_type: typing.Optional[ThothAdviserIntegrationEnum] = None,
) -> typing.Optional[tuple]:
    """Run advise in current directory, requires no arguments."""
    requirements_format = thoth_config.requirements_format
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

    pipfile = project.pipfile.to_string()
    pipfile_lock_str = project.pipfile_lock.to_string() if project.pipfile_lock else ""

    return advise(
        pipfile=pipfile,
        pipfile_lock=pipfile_lock_str,
        recommendation_type=recommendation_type,
        runtime_environment=runtime_environment,
        runtime_environment_name=runtime_environment_name,
        dev=dev,
        no_static_analysis=no_static_analysis,
        no_user_stack=no_user_stack,
        nowait=nowait,
        force=force,
        limit=limit,
        count=count,
        debug=debug,
        origin=origin,
        source_type=source_type,
        github_event_type=github_event_type,
        github_check_run_id=github_check_run_id,
        github_installation_id=github_installation_id,
        github_base_repo_url=github_base_repo_url,
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
    origin: str = None,
) -> typing.Optional[tuple]:
    """Submit a stack for provenance checks and wait for results."""
    if not pipfile:
        raise ValueError("No Pipfile content provided for provenance checks")

    stack = PythonStack(requirements=pipfile, requirements_lock=pipfile_lock)
    api_instance = ProvenanceApi(api_client)
    response = api_instance.post_provenance_python(
        stack, debug=debug, force=force, origin=origin
    )
    _LOGGER.info(
        "Successfully submitted provenance check analysis %r to %r",
        response.analysis_id,
        thoth_config.api_url,
    )

    _note_last_analysis_id(response.analysis_id)

    if nowait:
        return response.analysis_id

    _wait_for_analysis(is_analysis_ready, response.analysis_id)
    _LOGGER.debug("Retrieving provenance check result for %r", response.analysis_id)
    response = _retrieve_analysis_result(
        api_instance.get_provenance_python, response.analysis_id
    )
    if not response:
        return None

    _LOGGER.debug("Provenance check metadata: %r", response.metadata)
    return response.result["report"], response.result["error"]


def provenance_check_here(
    *,
    nowait: bool = False,
    force: bool = False,
    debug: bool = False,
    origin: str = None,
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

    _wait_for_analysis(is_analysis_ready, response.analysis_id)
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
    registry_user: str = None,
    registry_password: str = None,
    registry_verify_tls: bool = True,
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

    api_instance = BuildAnalysisApi(api_client)
    if registry_user or registry_password:
        # Swagger client handles None in a different way - we need to explicitly avoid passing
        # registry user and registry password if they are not set.
        response = api_instance.post_build(
            body=build_detail,
            debug=debug,
            registry_user=registry_user,
            registry_password=registry_password,
            registry_verify_tls=registry_verify_tls,
            force=force,
            environment_type=environment_type,
        )
    else:
        response = api_instance.post_build(
            body=build_detail,
            debug=debug,
            registry_verify_tls=registry_verify_tls,
            force=force,
        )

    _LOGGER.info("Successfully submitted build analysis to %r", thoth_config.api_url)
    if nowait:
        return response

    return response


@with_api_client
def get_log(api_client: ApiClient, analysis_id: str = None):
    """Get log of an analysis - the analysis type and endpoint are automatically derived from analysis id.

    If analysis_id is not provided, its get from the last thamos call which stores it in a temporary file.
    """
    if not analysis_id:
        analysis_id = _get_last_analysis_id()

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
                    message = colored(content["message"], "cyan")
                elif content["levelname"] == "INFO":
                    message = colored(content["message"], "green")
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
def get_status(api_client: ApiClient, analysis_id: str = None):
    """Get status of an analysis - the analysis type and endpoint are automatically derived from analysis id.

    If analysis_id is not provided, its get from the last thamos call which stores it in a temporary file.
    """
    if not analysis_id:
        analysis_id = _get_last_analysis_id()

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
def get_analysis_results(api_client: ApiClient, analysis_id: str):
    """Get the analysis result from a given id."""
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
        return response.result, response.result["error"]
    else:
        raise UnknownAnalysisType(
            "Cannot determine analysis type from identifier: %r", analysis_id
        )
