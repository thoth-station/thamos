#!/usr/bin/env python3
# thamos
# Copyright(C) 2022 Fridolin Pokorny
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

"""Configuration for Thamos CLI using rich-click."""

import os
import sys
import rich_click as click


def init_rich_click() -> None:
    """Initialize rich-click."""
    click.rich_click.ERRORS_EPILOGUE = (
        "Check Thamos documentation: https://thoth-station.ninja/docs/developers/thamos"
    )
    click.rich_click.HEADER_TEXT = "Thoth homepage: https://thoth-station.ninja"
    click.rich_click.FOOTER_TEXT = (
        "Check Thamos documentation: https://thoth-station.ninja/docs/developers/thamos"
    )
    click.rich_click.USE_RICH_MARKUP = True

    tool = os.path.basename(sys.argv[0])

    click.rich_click.COMMAND_GROUPS = {
        tool: [
            {
                "name": "Thoth resolver",
                "commands": [
                    "advise",
                    "environments",
                    "graph",
                    "images",
                    "indexes",
                    "log",
                    "provenance-check",
                    "status",
                    "whatprovides",
                ],
            },
            {
                "name": "Application & Requirements",
                "commands": [
                    "add",
                    "discover",
                    "install",
                    "purge",
                    "remove",
                    "run",
                    "venv",
                    "verify",
                ],
            },
            {
                "name": "Runtime environments",
                "commands": [
                    "check",
                    "config",
                    "list",
                    "show",
                ],
            },
            {
                "name": "Information",
                "commands": [
                    "support",
                    "version",
                ],
            },
        ],
    }
