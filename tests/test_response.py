#!/usr/bin/env python3
# thamos
# Copyright(C) 2019 - 2021 Fridolin Pokorny
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

from thoth.common import cwd
from thamos.lib import write_files


class TestResponse(ThamosTestCase):
    """Test response serialization."""

    def test_serialization(self, tmp_path: Path):
        """Test serialization of a response from backend."""
        response = json.loads((Path(self.data_dir) / "response_1.json").read_text())
        with cwd(str(tmp_path)):
            pipfile = response["result"]["report"]["products"][0]["project"][
                "requirements"
            ]
            pipfile_lock = response["result"]["report"]["products"][0]["project"][
                "requirements_locked"
            ]
            write_files(pipfile, pipfile_lock, requirements_format="pipenv")

            written_pipfile = toml.loads(Path("Pipfile").read_text())
            assert written_pipfile == {
                "dev-packages": {},
                "packages": {
                    "flask": {"index": "pypi-org", "version": "*"},
                    "tensorflow": {"index": "pypi-org", "version": "*"},
                },
                "source": [
                    {
                        "name": "pypi-org",
                        "url": "https://pypi.org/simple",
                        "verify_ssl": True,
                    }
                ],
                "thoth": {"allow_prereleases": {}, "disable_index_adjustment": False},
            }

            written_pipfile_lock = json.loads(Path("Pipfile.lock").read_text())
            assert written_pipfile_lock == pipfile_lock
