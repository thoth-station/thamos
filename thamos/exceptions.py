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

"""Exception hierarchy in Thamos."""


class ThamosException(Exception):
    """A base class for exceptions in Thamos."""


class NoProjectDirError(ThamosException):
    """An exception raised if the project directory cannot be found."""


class InternalError(ThamosException):
    """An exception raised on internal programming errors."""


class NoApiSupported(ThamosException):
    """Raised if client and Thoth server does not support same API versions."""


class ServiceUnavailable(ThamosException):
    """Raised if Thoth service is not available."""


class UnknownAnalysisType(ThamosException):
    """Raised analysis type (adviser, package-extract, ...) cannot be determined from analysis identifier."""


class NoRuntimeEnvironmentError(ThamosException):
    """An exception raised if no runtime environment could be found in configuration file."""


class RuntimeEnvironmentExistsError(ThamosException):
    """An exception raised the given runtime environment already exists."""


class NoRequirementsFormatError(ThamosException):
    """An exception raised if no requirements format could be found in configuration file."""


class ConfigurationError(ThamosException):
    """An exception raised if there are issues with configuration file."""


class TimeoutError(ThamosException):
    """An exception raised if the API takes longer than timeout limit."""


class ApiError(ThamosException):
    """An exception raised if the API doesn't return expected status code."""


class NoRequirementsFile(ThamosException):
    """An exception raised when requirements file is not present."""


class NoDevRequirements(ThamosException):
    """An exception raised if no development requirements are found during the installation process."""


class NoMatchingPackage(ThamosException):
    """An exception raised if no matching package can be found for a given import."""


class PedanticRunVerificationError(ThamosException):
    """An exception raised if the runtime environment used does not match configuration."""


class RequirementsFileError(ThamosException):
    """An exception raised if there is an issue with requirements file or lock file."""
