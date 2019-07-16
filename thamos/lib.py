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

from yaspin import yaspin
from yaspin.spinners import Spinners
from invectio import gather_library_usage

from . import __version__ as thamos_version
from .swagger_client.rest import ApiException
from .swagger_client import ApiClient
from .swagger_client import Configuration
from .swagger_client import PythonStack
from .swagger_client import RuntimeEnvironment
from .swagger_client import AdviseInput
from .swagger_client import AdviseApi
from .swagger_client import ImageAnalysisApi
from .swagger_client import ProvenanceApi
from .config import config as thoth_config
from .exceptions import UnknownAnalysisType

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


_LOGGER = logging.getLogger(__name__)
_LIBRARIES_USAGE = frozenset(("tensorflow", "keras", "pytorch"))


def with_api_client(func: typing.Callable):
    """Load configuration entries from Thoth configuration file."""
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
        api_client.user_agent = f"Thamos/{thamos_version} (Python {platform.python_version()}; " \
                                f"{platform.system()} {platform.release()})"
        result = func(api_client, *args, **kwargs)
        _LOGGER.debug("Elapsed seconds processing request: %f", monotonic() - start)
        return result

    return wrapper


def _wait_for_analysis(status_func: callable, analysis_id: str) -> None:
    """Wait for ongoing analysis to finish."""
    @contextmanager
    def _no_spinner():
        yield

    spinner = partial(
        yaspin,
        Spinners.clock,
        text=f"Waiting for response from Thoth (analysis: {analysis_id})...",
    )
    if _LOGGER.getEffectiveLevel() == logging.DEBUG or bool(
        int(os.getenv("THAMOS_NO_PROGRESSBAR", 1))
    ):
        # CLI automatically injects THAMOS_NO_PROGRESSBAR=0 if user did not turned it off explictily.
        spinner = _no_spinner

    sleep_time = 0.5
    with spinner():
        while True:
            response = status_func(analysis_id)
            if response.status.finished_at is not None:
                break
            _LOGGER.debug(
                "Waiting for %r to finish for %s seconds (state: %s)",
                analysis_id,
                sleep_time,
                response.status.state,
            )

            sleep(sleep_time)
            sleep_time = min(sleep_time * 2, 10)


def _retrieve_analysis_result(
    retrieve_func: callable, analysis_id: str
) -> typing.Optional[dict]:
    """Retrieve analysis result, raise error if analysis failed."""
    try:
        return retrieve_func(analysis_id)
    except ApiException as exc:
        _LOGGER.debug(
            "Retrieved error response %s from server: %s", exc.status, exc.reason
        )
        response = json.loads(exc.body)
        _LOGGER.debug("Error from server: %s", response)
        _LOGGER.error("%s (analysis: %s)", response["error"], analysis_id)
        return None


def _get_static_analysis() -> dict:
    """Get static analysis of files used in project."""
    # We are running in the root directory of project, use the root part for gathering static analysis.
    _LOGGER.info("Performing static analysis")
    try:
        library_usage = gather_library_usage(".", ignore_errors=True)
    except FileNotFoundError:
        _LOGGER.warning("No library usage was aggregated - no Python sources found")
        return {}

    result = {}
    for file_record in library_usage.values():
        for library, usage in file_record.items():
            if library not in _LIBRARIES_USAGE:
                _LOGGER.debug("Omitting usage of library %r", library)
                continue

            if library not in result:
                result[library] = []

            result[library].extend(usage)

    return result


@with_api_client
def advise(
    api_client: ApiClient,
    pipfile: str,
    pipfile_lock: str,
    recommendation_type: str = None,
    *,
    runtime_environment: dict = None,
    runtime_environment_name: str = None,
    limit_latest_versions: int = None,
    no_static_analysis: bool = False,
    nowait: bool = False,
    force: bool = False,
    limit: int = None,
    count: int = 1,
    debug: bool = False,
    origin: str = None,
) -> typing.Optional[tuple]:
    """Submit a stack for adviser checks and wait for results."""
    if not pipfile:
        raise ValueError("No Pipfile content provided for advises")

    if runtime_environment and runtime_environment_name:
        raise ValueError(
            "Cannot use runtime_environment and runtime_environment_name at the same time"
        )

    if runtime_environment is None:
        runtime_environment = thoth_config.get_runtime_environment(runtime_environment_name) or dict()

    # We use the explicit one if provided at the end.
    if limit_latest_versions is None:
        priority = (
            runtime_environment.pop("limit_latest_versions", None),
            thoth_config.content.get("limit_latest_versions", None),
            None
        )
        try:
            limit_latest_versions = next(filter(bool, priority))
        except StopIteration:
            limit_latest_versions = None

    if recommendation_type is None:
        priority = (
            runtime_environment.pop("recommendation_type", None),
            thoth_config.content.get("recommendation_type", None),
            "stable"
        )
        recommendation_type = next(filter(bool, priority))

    library_usage = None
    if not no_static_analysis:
        library_usage = _get_static_analysis()
        _LOGGER.debug("Library usage:\n%s", json.dumps(library_usage, indent=2))

    stack = PythonStack(requirements=pipfile, requirements_lock=pipfile_lock or "")

    if runtime_environment:
        # Override recommendation type specified explicitly in the runtime environment entry.
        runtime_environment.pop("recommendation_type", None)
        # Override latest versions limit specified explicitly in the runtime environment entry.
        runtime_environment.pop("limit_latest_versions", None)

        runtime_environment = RuntimeEnvironment(**runtime_environment)

    advise_input = AdviseInput(
        stack, runtime_environment=runtime_environment, library_usage=library_usage
    )
    api_instance = AdviseApi(api_client)

    if recommendation_type:
        recommendation_type = recommendation_type.lower()

    parameters = {
        "recommendation_type": recommendation_type,
        "debug": debug,
        "force": force,
    }

    if limit is not None:
        parameters["limit"] = limit

    if count is not None:
        parameters["count"] = count

    if limit_latest_versions is not None:
        parameters["limit_latest_versions"] = limit_latest_versions

    if origin is not None:
        parameters["origin"] = origin

    response = api_instance.post_advise_python(advise_input, **parameters)

    _LOGGER.info(
        "Successfully submitted advise analysis %r to %r",
        response.analysis_id,
        thoth_config.api_url,
    )

    _LOGGER.debug("Analysis parameters:\n%r", pprint.pformat(parameters))
    _LOGGER.debug("Adviser input:\n%s", advise_input.to_str())

    if nowait:
        return response.analysis_id

    _wait_for_analysis(api_instance.get_advise_python_status, response.analysis_id)
    _LOGGER.debug("Retrieving adviser result for %r", response.analysis_id)
    response = _retrieve_analysis_result(
        api_instance.get_advise_python, response.analysis_id
    )
    if not response:
        return None

    _LOGGER.debug("Adviser check metadata: %r", response.metadata)

    return response.result, response.result["error"]


def advise_here(
    recommendation_type: str = None,
    *,
    runtime_environment: dict = None,
    runtime_environment_name: str = None,
    limit_latest_versions: int = None,
    no_static_analysis: bool = False,
    nowait: bool = False,
    force: bool = False,
    limit: int = None,
    count: int = 1,
    debug: bool = False,
    origin: str = None,
) -> typing.Optional[tuple]:
    """Run advise in current directory, requires no arguments."""
    if not os.path.isfile("Pipfile"):
        raise FileNotFoundError("No Pipfile found in current directory")

    with open("Pipfile", "r") as pipfile:
        lock_str = ""
        if os.path.isfile("Pipfile.lock"):
            with open("Pipfile.lock", "r") as piplock:
                lock_str = piplock.read()

        return advise(
            pipfile=pipfile.read(),
            pipfile_lock=lock_str,
            recommendation_type=recommendation_type,
            runtime_environment_name=runtime_environment_name,
            limit_latest_versions=limit_latest_versions,
            no_static_analysis=no_static_analysis,
            nowait=nowait,
            force=force,
            limit=limit,
            count=count,
            debug=debug,
            origin=origin,
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
    response = api_instance.post_provenance_python(stack, debug=debug, force=force, origin=origin)
    _LOGGER.info(
        "Successfully submitted provenance check analysis %r to %r",
        response.analysis_id,
        thoth_config.api_url,
    )
    if nowait:
        return response.analysis_id

    _wait_for_analysis(api_instance.get_provenance_python_status, response.analysis_id)
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
) -> typing.Union[typing.Dict, str]:
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

    _wait_for_analysis(api_instance.get_analyze_status, response.analysis_id)
    _LOGGER.debug(
        "Retrieving image analysis result result for %r", response.analysis_id
    )
    response = _retrieve_analysis_result(api_instance.get_analyze, response.analysis_id)
    if not response:
        return None

    _LOGGER.debug("Image analysis metadata: %r", response.metadata)
    return response.result


@with_api_client
def get_log(api_client: ApiClient, analysis_id: str):
    """Get log of an analysis - the analysis type and endpoint are automatically derived from analysis id."""
    if analysis_id.startswith("package-extract-"):
        api_instance = ImageAnalysisApi(api_client)
        method = api_instance.get_analyze_log
    elif analysis_id.startswith("provenance-checker-"):
        api_instance = ProvenanceApi(api_client)
        method = api_instance.get_provenance_python_log
    elif analysis_id.startswith("adviser-"):
        api_instance = AdviseApi(api_client)
        method = api_instance.get_advise_python_log
    else:
        raise UnknownAnalysisType(
            "Cannot determine analysis type from identifier: %r", analysis_id
        )

    return method(analysis_id).log


@with_api_client
def get_status(api_client: ApiClient, analysis_id: str):
    """Get status of an analysis - the analysis type and endpoint are automatically derived from analysis id."""
    if analysis_id.startswith("package-extract-"):
        api_instance = ImageAnalysisApi(api_client)
        method = api_instance.get_analyze_status
    elif analysis_id.startswith("provenance-checker-"):
        api_instance = ProvenanceApi(api_client)
        method = api_instance.get_provenance_python_status
    elif analysis_id.startswith("adviser-"):
        api_instance = AdviseApi(api_client)
        method = api_instance.get_advise_python_status
    else:
        raise UnknownAnalysisType(
            "Cannot determine analysis type from identifier: %r", analysis_id
        )

    return method(analysis_id).status.to_dict()


@with_api_client
def get_analysis_results(api_client: ApiClient, analysis_id: str):
    """Get the analysis result from a given id."""
    if analysis_id.startswith("package-extract-"):
        api_instance = ImageAnalysisApi(api_client)
        method = api_instance.get_analyze
        response = _retrieve_analysis_results(method, analysis_id)
        return response.result
    elif analysis_id.startswith("provenance-checker-"):
        api_instance = ProvenanceApi(api_client)
        method = api_instance.get_provenance_python
        response = _retrieve_analysis_result(method, analysis_id)
        return response.result["report"], response.result["error"]
    elif analysis_id.startswith("adviser-"):
        api_instance = AdviseApi(api_client)
        method = api_instance.get_advise_python
        response = _retrieve_analysis_result(
            api_instance.get_advise_python, analysis_id
        )
        return response.result, response.result["error"]
    else:
        raise UnknownAnalysisType(
            "Cannot determine analysis type from identifier: %r", analysis_id
        )
