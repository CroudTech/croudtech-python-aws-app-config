# -*- coding: utf-8 -*-
"""
    Setup file for croudtech_python_aws_app_config.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 3.2.3.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import importlib.machinery
import importlib.metadata
import importlib.resources
import importlib.util
import sys

from setuptools import setup
import importlib


try:
    spec = importlib.metadata.distribution("setuptools")

except importlib.metadata.PackageNotFoundError as err:
    print(err)
    print("Error: version of setuptools is too old (<69.5.1)!")
    sys.exit(1)

with open("requirements.txt") as f:
    required = f.read().splitlines()

if __name__ == "__main__":
    setup(
        install_requires=required,
        use_pyscaffold=True,
        entry_points={
            "console_scripts": [
                "croudtech-app-config=croudtech_python_aws_app_config.cli:cli"
            ],
        },
        packages=["croudtech_python_aws_app_config"],
    )
