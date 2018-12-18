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

"""CLI and library configuration."""

import logging
import os

import click
import requests
import yaml

from .utils import workdir
from .exceptions import NoApiSupported
from .exceptions import InternalError


_LOGGER = logging.getLogger(__name__)


class _Configuration:
    """Handling of Thoth's configuration."""

    DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
    DEFAULT_THOTH_CONFIG = os.path.join(DATA_DIR, 'defaultThoth.yaml')
    CONFIG_NAME = '.thoth.yaml'

    def __init__(self):
        """Construct configuration instance."""
        self._configuration = None
        self._index_aicoe = None
        # Thoth instance to be used when explicitly said by user - the one stated in
        # configuration file will be omitted.
        self.explicit_host = None
        self._api_url = None
        self._tls_verify = True

    @property
    def api_url(self):
        return self._api_url

    @property
    def tls_verify(self):
        return self._tls_verify

    @property
    def content(self):
        """Access configuration."""
        if not self._configuration:
            self.load_config()

        return self._configuration

    def load_config(self):
        """Load configuration file."""
        with workdir(config.CONFIG_NAME):
            with open(config.CONFIG_NAME, 'r') as config_file:
                self._configuration = yaml.safe_load(config_file)

    def create_default_config(self):
        """Place default configuration into the current directory."""
        if not os.path.isdir('.git'):
            _LOGGER.warning("Configuration file is not created in the root of git repo")

        _LOGGER.debug("Reading default configuration from %r", self.DEFAULT_THOTH_CONFIG)
        with open(self.DEFAULT_THOTH_CONFIG, 'r') as default_config_file:
            default_config = default_config_file.read()

        _LOGGER.debug("Writing configuration file to %r", os.path.join(os.getcwd(), self.CONFIG_NAME))
        with open(self.CONFIG_NAME, 'w') as config_file:
            config_file.write(default_config)

    @staticmethod
    def open_config_file():
        """Open Thoth's configuration file."""
        with workdir(config.CONFIG_NAME):
            _LOGGER.debug("Opening configuration file %r", config.CONFIG_NAME)
            click.edit(filename=config.CONFIG_NAME)

    def api_discovery(self, host: str = None) -> str:
        """Discover API versions available, return the most recent one supported by client and server."""
        api_url = 'https://' + host + '/api/v1'
        self._tls_verify = self.content.get('tls_verify', True)

        response = requests.get(api_url, verify=self.tls_verify, headers={'Accept': 'application/json'})

        try:
            response.raise_for_status()
            if not self.tls_verify:
                _LOGGER.warning(
                    "TLS verification turned off, its highly recommended to use a secured connection, "
                    "see configuration file for configuration options"
                )
        except Exception:
            # Try without TLS - maybe router was not configured to use TLS.
            api_url = 'http://' + host + '/api/v1'
            response = requests.get(api_url, headers={'Accept': 'application/json'})
            try:
                response.raise_for_status()
                _LOGGER.warning(
                    "Using insecure connection to API service, please contact service provider to "
                    "install TLS in order to secure network traffic"
                )
            except Exception as exc:
                raise NoApiSupported("Server does not support API v1 required by Thamos client") from exc

        if response.status_code != 200:
            raise InternalError("Cannot correctly determine API version to be used")

        self._api_url = api_url
        return self._api_url


config = _Configuration()
