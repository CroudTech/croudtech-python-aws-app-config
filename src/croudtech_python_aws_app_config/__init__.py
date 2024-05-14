# -*- coding: utf-8 -*-
from importlib import resources, metadata

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "croudtech-python-aws-app-config"
    __version__ = metadata.distribution(dist_name).version
except metadata.PackageNotFoundError:
    __version__ = "unknown"
