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

"""Utility and helper functions for Thamos."""

from typing import Optional
from contextlib import contextmanager
import logging
import os
import sys

from thoth.common import cwd

from .exceptions import NoProjectDirError

# Limit traversing to parent directories so we handle root - we do not loop over and over in root and we also
# handle cyclic symlinks natively.
_WORKDIR_DEPTH_LEN = 33
_LOGGER = logging.getLogger(__name__)


@contextmanager  # type: ignore
def workdir(file_lookup: Optional[str] = None, warn_on_dir_change: bool = True) -> None:
    """Find project directory and cd into it."""
    file_lookup = file_lookup or ".thoth.yaml"

    project_dir = os.getcwd()
    original_project_dir = project_dir
    for _ in range(_WORKDIR_DEPTH_LEN):
        file = os.path.join(project_dir, file_lookup)
        if os.path.isfile(file):
            with cwd(project_dir):
                if project_dir != original_project_dir and warn_on_dir_change:
                    _LOGGER.warning("Using %r as project root directory", project_dir)
                yield project_dir
            break

        project_dir = os.path.dirname(project_dir)
    else:
        raise NoProjectDirError(
            f"No {file_lookup} found in the current directory {os.getcwd()!r} or in any of its parent "
            f"directories, you can generate it using '{sys.argv[0]} config'"
        )
