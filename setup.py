#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This file is part of Viper - https://github.com/viper-framework/viper
# See the file 'LICENSE' for copying permission.

import os
from setuptools import setup

# TODO - this requires viper-framework to be installed first
from viper.common.version import __version__

__description__ = "Web interface for the Viper Binary Analysis & Management Framework"

def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, "__init__.py"))]

def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, "", 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, "__init__.py"))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

def get_requirements():
    """
    Return all requirements from necessary files.
    """
    requirement_files = [
        #"requirements-base.txt",
        #"requirements-modules.txt",
        #"requirements-web.txt"
        'requirements.txt'
    ]

    requires = []
    for file_name in requirement_files:
        with open(file_name) as handle:
            for line in handle:
                line = line.strip()
                if line == "" or line.startswith("#"):
                    continue

                requires.append(line)

    return requires
setup(
    name="viper_web",
    version=__version__,
    author="Claudio Guarnieri",
    author_email="nex@nex.sx",
    description=__description__,
    long_description=__description__,
    url="http://viper.li",
    platforms="any",
    scripts= ["viper-web"],
    packages=get_packages("viper_web"),
    package_data=get_package_data("viper_web"),
    include_package_data=True,
    install_requires=get_requirements(),
    zip_safe=False,
    tests_require=["pytest"],
    # BSD 3-Clause License:
    # - http://choosealicense.com/licenses/bsd-3-clause
    # - http://opensource.org/licenses/BSD-3-Clause
    license="BSD 3-Clause",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Topic :: Security",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: POSIX :: Linux",
    ],
    keywords="binary analysis management malware research",
)

