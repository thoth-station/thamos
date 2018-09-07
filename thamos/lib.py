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

from .swagger_client import ApiClient
from .swagger_client import Configuration
from .swagger_client import ProvenanceApi
from .swagger_client import PythonStack
from .swagger_client import RecommendationApi
from .config import config as thoth_config

_LOGGER = logging.getLogger(__name__)


def with_api_client(func):
    """Load configuration entries from Thoth configuration file."""
    def wrapper(*args, **kwargs):
        thoth_config.load_config()
        config = Configuration()
        config.host = thoth_config.content.get('host') or config.host
        return func(ApiClient(configuration=config), *args, **kwargs)

    return wrapper


@with_api_client
def advise(api_client: ApiClient, pipfile: str, pipfile_lock: str, debug: bool = False) -> tuple:
    """Submit a stack for adviser checks and wait for results."""
    stack = PythonStack(requirements=pipfile, requirements_lock=pipfile_lock)
    api_instance = RecommendationApi(api_client)
    response = api_instance.post_recommend_python(
        stack,
        type=thoth_config.content.get('recommendation_type', 'stable'),
        debug=debug
    )
    print(response)
    # TODO: implement models on API and wait for analysis to finish
    return None, None, None


@with_api_client
def provenance_check(api_client: ApiClient, pipfile: str, pipfile_lock: str, debug: bool = False) -> tuple:
    """Submit a stack for provenance checks and wait for results."""
    stack = PythonStack(requirements=pipfile, requirements_lock=pipfile_lock)
    api_instance = ProvenanceApi(api_client)
    response = api_instance.post_provenance_python(stack, debug=debug)
    print(response)
    # TODO: implement models on API and wait for analysis to finish
    # TODO: accept debug on API
    return None, None, None
