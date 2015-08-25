# Tests for the natural order sorting package.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: August 25, 2015
# URL: https://github.com/xolox/python-naturalsort

"""Tests for the natural order sorting package."""

# Standard library modules.
import unittest

# The module we're testing.
from natsort import natsort


class NaturalSortTestCase(unittest.TestCase):

    """Container for the `naturalsort` tests."""

    def test_plain_old_sorting(self):
        """Test plain old sorting (what we don't want)."""
        assert sorted(['1', '5', '10', '50']) == ['1', '10', '5', '50']

    def test_version_sorting(self):
        """Test version sorting (what we're after)."""
        assert natsort(['1', '5', '10', '50']) == ['1', '5', '10', '50']

    def test_reversed_version_sorting(self):
        """Test reversed version sorting."""
        assert natsort(['1', '5', '10', '50'], reverse=True) == ['50', '10', '5', '1']

    def test_dotted_sorting(self):
        """
        Test a previously fixed bug to prevent regressions.

        I've purposefully shuffled the order on the left side to avoid false
        positives caused by stable sorting.
        """
        assert natsort(['1.5', '1.0']) == ['1.0', '1.5']

    def test_python_3_compatibility(self):
        """
        Test the Python 3 incompatibility reported in `issue 2`_.

        .. _issue 2: https://github.com/xolox/python-naturalsort/issues/2
        """
        assert natsort(['1', 'a']) == ['1', 'a']
