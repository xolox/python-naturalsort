#!/bin/bash -e

# Test driver for old Python versions.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: November 2, 2015
# URL: https://github.com/xolox/python-naturalsort
#
# Recent versions of the `virtualenv' and `tox' packages have dropped support
# for Python 2.4 and Python 2.5 and thus running test suites against these
# Python versions has become a non-trivial exercise... Fortunately because the
# `naturalsort' package has no external dependencies we don't actually need a
# virtual environment!

for python in python2.{4,5}; do
  if which $python &>/dev/null; then
    echo "Running tests against $python .." >&2
    PYTHONPATH="$PWD" $python natsort/tests.py
  fi
done
