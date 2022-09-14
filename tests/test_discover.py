#!/usr/bin/env python3
# thamos
# Copyright(C) 2022 Maya Costantini
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


"""Tests for the thamos discover command implementation."""

import mock

from thoth.analyzer import CommandResult
from thoth.analyzer import run_command
from thamos import discover

from base import ThamosTestCase


_CUDA_VERSION_OUTPUT = '"nvcc: NVIDIA (R) Cuda compiler driver\n Copyright (c) 2005-2015 NVIDIA Corporation\n Built on Mon_Feb_16_22:59:02_CST_2015\n Cuda compilation tools, release 7.0, V7.0.27"'  # noqa
_CUDNN_HEADERS_OUTPUT = '"#define CUDNN_MAJOR 7\n #define CUDNN_MINOR 5\n #define CUDNN_PATCHLEVEL 0\n #define CUDNN_VERSION (CUDNN_MAJOR * 1000 + CUDNN_MINOR * 100 + CUDNN_PATCHLEVEL)"'  # noqa
_OPENBLAS_RPM_OUTPUT = (
    '"openblas-0.3.15-3.el8.x86_64\n openblas-srpm-macros-2-2.el8.noarch"'
)
_OPENMPI_RPM_OUTPUT = '"openmpi-devel-4.1.1-3.el8.x86_64\n openmpi-4.1.1-3.el8.x86_64"'
_MKL_PIPY_OUTPUT = '"mkl                               2022.1.0"'
_LSPCI_OUTPUT = '"00:02.0 VGA compatible controller: Intel Corporation CometLake-U GT2 [UHD Graphics] (rev 02)"'


def _mock_run_command_available(*args, **kwargs) -> CommandResult:
    """Mock run_command when information is available."""
    if args[0] == "nvcc --version":
        return run_command(f"echo {_CUDA_VERSION_OUTPUT}")

    if args[0].endswith("grep CUDNN_MAJOR -A 10"):
        return run_command(f"echo {_CUDNN_HEADERS_OUTPUT}")

    if args[0] == "pip list | grep -F mkl":
        return run_command(f"echo {_MKL_PIPY_OUTPUT}")

    if args[0] == "rpm -qa | grep openblas":
        return run_command(f"echo {_OPENBLAS_RPM_OUTPUT}")

    if args[0] == "rpm -qa | grep openmpi":
        return run_command(f"echo {_OPENMPI_RPM_OUTPUT}")

    if args[0] == "lspci | grep VGA":
        return run_command(f"echo {_LSPCI_OUTPUT}")


def _mock_run_command_not_found(*args, **kwargs) -> CommandResult:
    """Mock run_command when information is not found."""
    if args[0] == "nvcc --version":
        return run_command("exit 127", raise_on_error=False)

    if args[0].endswith("grep CUDNN_MAJOR -A 10"):
        return run_command("exit 1", raise_on_error=False)

    if args[0] == "pip list | grep -F mkl":
        return run_command("exit 1", raise_on_error=False)

    if args[0] == "rpm -qa | grep openblas":
        return run_command("exit 1", raise_on_error=False)

    if args[0] == "rpm -qa | grep openmpi":
        return run_command("exit 1", raise_on_error=False)

    if args[0] == "lspci | grep VGA":
        return run_command("exit 1", raise_on_error=False)


class TestDiscover(ThamosTestCase):
    """Tests for the thamos discover command."""

    @mock.patch("thamos.discover.run_command", new=_mock_run_command_available)
    def test_discover_cuda_version_present(self) -> None:
        """Test discovering CUDA version if present in environment."""
        with mock.patch("thamos.discover.run_command", new=_mock_run_command_available):
            with mock.patch("os.environ", {"THAMOS_DISABLE_CUDA": "0"}):
                assert discover.discover_cuda_version() == "7.0"

    @mock.patch("thamos.discover.run_command", new=_mock_run_command_not_found)
    def test_discover_cuda_version_not_present(self):
        """Test discovering CUDS version if not present in environment."""
        with mock.patch("os.environ", {"THAMOS_DISABLE_CUDA": "1"}):
            assert discover.discover_cuda_version() is None

    def test_discover_distribution(self) -> None:
        """Test discovering distribution."""
        with mock.patch("distro.linux_distribution") as mock_distribution:
            mock_distribution.return_value = ("rhel", "8.5", "Ootpa")
            assert discover.discover_distribution() == ("rhel", "8")

    def test_discover_python_version(self) -> None:
        """Test discovering Python version."""
        with mock.patch("sys.version_info") as mock_sys_version_info:
            mock_sys_version_info.major, mock_sys_version_info.minor = "3", "8"
            assert discover.discover_python_version() == "3.8"

            mock_sys_version_info.major, mock_sys_version_info.minor = "3", "10"
            assert discover.discover_python_version() == "3.10"

    def test_discover_cpu(self) -> None:
        """Test discovering CPU."""
        test_cpu_info_correct = {
            "cpu_family": 6,
            "cpu_model": 142,
            "cpu_model_name": "Intel(R) Core(TM) i7-10610U CPU @ 1.80GHz",
        }

        test_cpu_info_wrong = {
            "cpu_family": 7,
            "cpu_model": 142,
            "cpu_model_name": "Intel(R) Core(TM) i7-10610U CPU @ 1.60GHz",
        }

        with mock.patch("thamos.discover._PROC_CPU_INFO", "tests/data/cpu_info_file"):
            assert discover.discover_cpu() == test_cpu_info_correct
            assert discover.discover_cpu() != test_cpu_info_wrong

    def test_discover_platform(self) -> None:
        """Test discover platform."""
        with mock.patch("sysconfig.get_platform") as mock_get_platform:
            mock_get_platform.return_value = "linux-x86_64"
            assert discover.discover_platform() == "linux-x86_64"

    def test_discover_base_image(self) -> None:
        """Test discovering base image."""

        def getenv_image(env_variable: str, *args) -> str:
            mock_env = {
                "IMAGE_NAME": "s2i-thoth-ubi8-py38",
                "THOTH_S2I_NAME": "quay.io/thoth-station/s2i-thoth-ubi8-py38",
                "THOTH_S2I_VERSION": "0.33.0",
                "IMAGE_TAG": "0.33.0",
            }
            return mock_env.get(env_variable)

        with mock.patch("os.getenv", side_effect=getenv_image):
            assert discover.discover_base_image() == "s2i-thoth-ubi8-py38:0.33.0"

    @mock.patch("thamos.discover.run_command", new=_mock_run_command_available)
    def test_discover_cudnn_version_available(self) -> None:
        """Test discover CuDNN version when present in environment."""
        assert discover.discover_cudnn_version() == "7.5.0"

    @mock.patch("thamos.discover.run_command", new=_mock_run_command_not_found)
    def test_discover_cudnn_version_not_found(self) -> None:
        """Test discover CuDNN version when not present in environment."""
        assert discover.discover_cudnn_version() is None

    @mock.patch("thamos.discover.run_command", new=_mock_run_command_available)
    def test_discover_mkl_available(self) -> None:
        """Test discover MKL Python package version when present in environment."""
        assert discover.discover_mkl_version() == "2022.1.0"

    @mock.patch("thamos.discover.run_command", new=_mock_run_command_not_found)
    def test_discover_mkl_not_found(self) -> None:
        """Test discover MKL Python package version when not present in environment."""
        assert discover.discover_mkl_version() is None

    @mock.patch("thamos.discover.run_command", new=_mock_run_command_available)
    def test_discover_openblas_available(self) -> None:
        """Test discover OpenBLAS as an RPM package when present in environment."""
        assert discover.discover_rpm_package("openblas") == {
            "name": "openblas",
            "version": "0.3.15",
            "release": "3.el8",
            "epoch": "",
            "architecture": "x86_64",
        }

    @mock.patch("thamos.discover.run_command", new=_mock_run_command_not_found)
    def test_discover_openblas_not_found(self) -> None:
        """Test discover OpenBLAS as an RPM package when not present in environment."""
        assert discover.discover_rpm_package("openblas") is None

    @mock.patch("thamos.discover.run_command", new=_mock_run_command_available)
    def test_discover_openmpi_available(self) -> None:
        """Test discover OpenMPI as an RPM package when present in environment."""
        assert discover.discover_rpm_package("openmpi") == {
            "name": "openmpi",
            "version": "4.1.1",
            "release": "3.el8",
            "epoch": "",
            "architecture": "x86_64",
        }

    @mock.patch("thamos.discover.run_command", new=_mock_run_command_not_found)
    def test_discover_openmpi_not_found(self) -> None:
        """Test discover OpenMPI as an RPM package when not present in environment."""
        assert discover.discover_rpm_package("openmpi") is None

    @mock.patch("thamos.discover.run_command", new=_mock_run_command_available)
    def test_discover_gpu_model_available(self) -> None:
        """Test discover GPU model when present in environment."""
        assert (
            discover.discover_gpu_model()
            == "VGA compatible controller: Intel Corporation CometLake-U GT2 [UHD Graphics] (rev 02)"
        )

    @mock.patch("thamos.discover.run_command", new=_mock_run_command_not_found)
    def test_discover_gpu_model_not_found(self) -> None:
        """Test discover GPU model when not present in environment."""
        assert discover.discover_gpu_model() is None
