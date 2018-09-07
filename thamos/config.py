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
from subprocess import call

import yaml

from .utils import workdir

_LOGGER = logging.getLogger(__name__)


class _Configuration:
    """Handling of Thoth's configuration."""

    DATA_DIR = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'data')
    DEFAULT_THOTH_CONFIG = os.path.join(DATA_DIR, 'defaultThoth.yaml')
    CONFIG_NAME = '.thoth.yaml'

    def __init__(self):
        """Construct configuration instance."""
        self._configuration = None

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
                self._configuration = yaml.load(config_file)

    def create_default_config(self):
        """Place default configuration into the current directory."""
        if not os.path.isdir('.git'):
            _LOGGER.warning(
                "Configuration file is not created in the root of git repo")

        _LOGGER.debug("Reading default configuration from %r",
                      self.DEFAULT_THOTH_CONFIG)
        with open(self.DEFAULT_THOTH_CONFIG, 'r') as default_config_file:
            default_config = default_config_file.read()

        _LOGGER.debug("Writing configuration file to %r",
                      os.path.join(os.getcwd(), self.CONFIG_NAME))
        with open(self.CONFIG_NAME, 'w') as config_file:
            config_file.write(default_config)

    @staticmethod
    def open_config_file():
        """Open Thoth's configuration file."""
        with workdir(config.CONFIG_NAME):
            editor = os.getenv('EDITOR', 'vim')
            _LOGGER.debug(
                "Opening configuration file %r with editor %r", config.CONFIG_NAME, editor)
            call([editor, config.CONFIG_NAME])


config = _Configuration()
