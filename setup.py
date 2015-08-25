#!/usr/bin/env python

"""Setup script for the `naturalsort` package."""

# Author: Peter Odding <peter@peterodding.com>
# Last Change: August 25, 2015
# URL: https://github.com/xolox/python-naturalsort

# Standard library modules.
import codecs
import os
import sys

# De-facto standard solution for Python packaging.
from setuptools import find_packages, setup

# Find the directory where the source distribution was unpacked.
source_directory = os.path.dirname(os.path.abspath(__file__))

# Add the directory with the source distribution to the search path.
sys.path.append(source_directory)

# Import the module to find the version number (this is safe because we don't
# have any external dependencies).
from natsort import __version__ as version_string

# Fill in the long description (for the benefit of PyPI)
# with the contents of README.rst (rendered by GitHub).
readme_file = os.path.join(source_directory, 'README.rst')
with codecs.open(readme_file, 'r', 'utf-8') as handle:
    readme_text = handle.read()

setup(
    name='naturalsort',
    version=version_string,
    description="Simple natural order sorting API for Python",
    long_description=readme_text,
    url='https://github.com/xolox/python-naturalsort',
    author='Peter Odding',
    author_email='peter@peterodding.com',
    packages=find_packages(),
    test_suite='natsort.tests',
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration',
        'Topic :: Text Processing :: General',
    ])
