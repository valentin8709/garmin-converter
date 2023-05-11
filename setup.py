#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""Setup module for Garmin Converter."""

from pathlib import Path
from setuptools import setup, find_packages
import garmin_converter

HERE = Path(__file__).parent
README = (HERE / "README.md").read_text()
APP_VERSION = appinfos.__version__

setup(
    name='garmin_converter',
    description='Convert FIT Garmin format to GPX using fit2gpx library.',
    version=APP_VERSION,
    author="Valou",
    packages=find_packages(),
    author_email="no_email@antispam.com",
    long_description=README,
    python_requires=">=3.7",
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'License :: DWTFYW', 'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7'
    ],
    entry_points={
        'console_scripts': ['garmin_converter = garmin_converter.garmin_converter:main']},
    zip_safe=False,
    install_requires=[
        'fit2gpx',
    ]
)
