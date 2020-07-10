"""This file sets up the thoth-thamos module."""

import os
import sys
from setuptools import setup, find_packages
from pathlib import Path
from setuptools.command.test import test as TestCommand  # noqa


def get_install_requires():
    """Get thamos installation requirements."""
    with open("requirements.txt", "r") as requirements_file:
        return [req for req in requirements_file.readlines() if req]


def get_version():
    """Get thamos version."""
    with open(os.path.join("thamos", "__init__.py")) as f:
        content = f.readlines()

    for line in content:
        if line.startswith("__version__ ="):
            # dirty, remove trailing and leading chars
            return line.split(" = ")[1][1:-2]
    raise ValueError("No version identifier found")


class Test(TestCommand):
    """Introduce test command to run testsuite using pytest."""

    _IMPLICIT_PYTEST_ARGS = [
        "tests/",
        "--timeout=2",
        "--cov=./thamos",
        "--capture=no",
        "--verbose",
        "-l",
        "-s",
        "-vv",
    ]

    user_options = [("pytest-args=", "a", "Arguments to pass into py.test")]

    def initialize_options(self):
        """Initialize cli options."""
        super().initialize_options()
        self.pytest_args = None

    def finalize_options(self):
        """Finalize cli options."""
        super().finalize_options()
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Run pytests."""
        import pytest  # noqa

        passed_args = list(self._IMPLICIT_PYTEST_ARGS)

        if self.pytest_args:
            self.pytest_args = [arg for arg in self.pytest_args.split() if arg]
            passed_args.extend(self.pytest_args)

        sys.exit(pytest.main(passed_args))


VERSION = get_version()
setup(
    name="thamos",
    entry_points={"console_scripts": ["thamos=thamos.cli:cli"]},
    version=VERSION,
    package_data={"thamos": [os.path.join("data", "*.yaml")]},
    include_package_data=True,
    description="A CLI tool and library for interacting with Thoth",
    long_description=Path("README.rst").read_text(),
    author="Fridolin Pokorny",
    author_email="fridolin@redhat.com",
    license="GPLv3+",
    packages=find_packages(),
    long_description_content_type="text/x-rst",
    cmdclass={"test": Test},
    install_requires=get_install_requires(),
    command_options={
        "build_sphinx": {
            "version": ("setup.py", VERSION),
            "release": ("setup.py", VERSION),
        }
    },
)
