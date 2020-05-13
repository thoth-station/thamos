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

"""Utility and helper functions for Thamos."""

from contextlib import contextmanager
import os
import sys

from .exceptions import NoProjectDirError

# Limit traversing to parent directories so we handle root - we do not loop over and over in root and we also
# handle cyclic symlinks natively.
_WORKDIR_DEPTH_LEN = 33


@contextmanager
def workdir(file_lookup: str = None):
    """Find project directory and cd into it."""
    file_lookup = file_lookup or ".thoth.yaml"

    project_dir = os.getcwd()
    for _ in range(_WORKDIR_DEPTH_LEN):
        file = os.path.join(project_dir, file_lookup)
        if os.path.isfile(file):
            with cwd(project_dir):
                yield project_dir
            break

        project_dir = os.path.dirname(project_dir)
    else:
        raise NoProjectDirError(
            f"No {file_lookup} found in the current directory {os.getcwd()!r} or in any of its parent "
            f"directories, you can generate it using '{sys.argv[0]} config'"
        )


@contextmanager
def cwd(target):
    """Manage cwd in a pushd/popd fashion."""
    curdir = os.getcwd()
    os.chdir(target)
    try:
        yield curdir
    finally:
        os.chdir(curdir)
