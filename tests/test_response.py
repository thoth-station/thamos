#!/usr/bin/env python3
# thamos
# Copyright(C) 2019, 2020 Fridolin Pokorny
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

"""Test serialization of response from Thoth."""

import json
from base import ThamosTestCase
from pathlib import Path
import toml

from thamos.utils import cwd
from thamos.cli import _write_files


class TestResponse(ThamosTestCase):
    """Test response serialization."""

    def test_serialization(self, tmp_path: Path):
        """Test serialization of a response from backend."""
        response = json.loads((Path(self.data_dir) / "response_1.json").read_text())
        with cwd(str(tmp_path)):
            pipfile = response["report"][0][1]["requirements"]
            pipfile_lock = response["report"][0][1]["requirements_locked"]
            _write_files(pipfile, pipfile_lock, requirements_format="pipenv")

            written_pipfile = toml.loads(Path("Pipfile").read_text())
            assert written_pipfile == pipfile

            written_pipfile_lock = json.loads(Path("Pipfile.lock").read_text())
            assert written_pipfile_lock == pipfile_lock
