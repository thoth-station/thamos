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

"""Core parts of library for interacting with Thoth."""

import logging
from time import sleep

from .swagger_client import ApiClient
from .swagger_client import Configuration
from .swagger_client import ProvenanceApi
from .swagger_client import PythonStack
from .swagger_client import AdviseApi
from .config import config as thoth_config

_LOGGER = logging.getLogger(__name__)


def with_api_client(func):
    """Load configuration entries from Thoth configuration file."""
    def wrapper(*args, **kwargs):
        thoth_config.load_config()
        config = Configuration()
        config.host = thoth_config.content.get('host') or config.host
        _LOGGER.debug("Using Thoth host %r", config.host)
        return func(ApiClient(configuration=config), *args, **kwargs)

    return wrapper


def _wait_for_analysis(status_func: callable, analysis_id) -> None:
    """Wait for ongoing analysis to finish."""
    sleep_time = 0.5
    while True:
        response = status_func(analysis_id)
        if response.status['finished_at'] is not None:
            break
        _LOGGER.debug("Waiting for %r to finish for %s seconds", analysis_id, sleep_time)

        sleep(sleep_time)
        sleep_time = min(sleep_time * 2, 10)


@with_api_client
def advise(api_client: ApiClient, pipfile: str, pipfile_lock: str, debug: bool = False) -> tuple:
    """Submit a stack for adviser checks and wait for results."""
    stack = PythonStack(requirements=pipfile, requirements_lock=pipfile_lock or '')
    api_instance = AdviseApi(api_client)
    response = api_instance.post_advise_python(
        stack,
        recommendation_type=thoth_config.content.get('recommendation_type', 'stable'),
        debug=debug
    )
    _LOGGER.debug("Sucessfully submitted advise analysis; id is %r", response.analysis_id)
    _wait_for_analysis(api_instance.get_advise_python_status, response.analysis_id)
    _LOGGER.debug("Retrieving adviser result for %r", response.analysis_id)
    response = api_instance.get_advise_python(response.analysis_id)
    _LOGGER.debug("Adviser check metadata: %r", response.metadata)

    result = response.result
    return None, None, None


@with_api_client
def provenance_check(api_client: ApiClient, pipfile: str, pipfile_lock: str, debug: bool = False) -> tuple:
    """Submit a stack for provenance checks and wait for results."""
    stack = PythonStack(requirements=pipfile, requirements_lock=pipfile_lock)
    api_instance = ProvenanceApi(api_client)
    response = api_instance.post_provenance_python(stack, debug=debug)
    _LOGGER.debug("Sucessfully submitted provenance check analysis; id is %r", response.analysis_id)
    _wait_for_analysis(api_instance.get_provenance_python_status, response.analysis_id)
    _LOGGER.debug("Retrieving provenance check result for %r", response.analysis_id)
    response = api_instance.get_provenance_python(response.analysis_id)
    _LOGGER.debug("Provenance check metadata: %r", response.metadata)

    result = response.result
    return None, None, None
