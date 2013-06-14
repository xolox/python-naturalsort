#!/usr/bin/env python

# Tests for natural order sorting module.
#
# Author: Peter Odding <peter.odding@paylogic.eu>
# Last Change: June 14, 2013
# URL: https://pypi.python.org/pypi/naturalsort

# Standard library modules.
import unittest

# The module we're testing.
from natsort import natsort

class PipAccelTestCase(unittest.TestCase):

    def runTest(self):

      # This is plain old sorting (what we don't want).
      assert sorted(['1', '5', '10', '50']) == ['1', '10', '5', '50']

      # This is version sorting (what we're after).
      assert natsort(['1', '5', '10', '50']) == ['1', '5', '10', '50']

      # This covers a previously fixed bug.
      assert natsort(['1.0', '1.5']) == ['1.0', '1.5']
