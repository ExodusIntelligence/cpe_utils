#!/usr/bin/env python
# encoding: utf-8

import os, sys
from setuptools import setup

setup(
    # metadata
    name='cpe_utils',
    description='A CPE utility library',
    long_description="""
        A CPE utility library that provides utility functions for
        expanding CPE wildcards, matching CPEs, etc.
    """,
    license='MIT',
    version='0.1.0',
    author='Exodus Intelligence: Mark Jones, Calvin Hooper, Noe Ortega, James Johnson',
    maintainer='Exodus Intelligence',
    author_email='eng@exodusintel.com',
    url='https://github.com/ExodusIntelligence/cpe_utils',
    platforms='Cross Platform',
    download_url="https://github.com/ExodusIntelligence/cpe_utils/tarball/v1.0.0",
    install_requires = open(os.path.join(os.path.dirname(__file__), "requirements.txt")).read().split("\n"),
    classifiers = [
        'Programming Language :: Python :: 2',
    #    'Programming Language :: Python :: 3',
    ],
    packages=['cpe_utils'],
)
