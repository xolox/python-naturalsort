# Tests for the natural order sorting package.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: November 2, 2015
# URL: https://github.com/xolox/python-naturalsort

"""Tests for the natural order sorting package."""

# Standard library modules.
import random
import unittest

# The module we're testing.
from natsort import NaturalOrderKey, natsort


class NaturalSortTestCase(unittest.TestCase):

    """Container for the `naturalsort` tests."""

    def test_plain_old_sorting(self):
        """Test plain old sorting (what we don't want :-)."""
        assert sorted(['1', '5', '10', '50']) == ['1', '10', '5', '50']

    def test_version_sorting(self):
        """Test version sorting (what we're after)."""
        assert natsort(['1', '5', '10', '50']) == ['1', '5', '10', '50']

    def test_reversed_version_sorting(self):
        """Test reversed version sorting."""
        assert natsort(['1', '5', '10', '50'], reverse=True) == ['50', '10', '5', '1']

    def test_zero_padding(self):
        """Test that zero padding semantics are respected."""
        assert natsort(['1.5.1', '1.5']) == ['1.5', '1.5.1']

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

    def test_more_complex_versions(self):
        """
        Test the implementation of the ``NaturalOrderKey`` class.

        This test uses some more complex version strings that were sorted
        incorrectly by the initial (way too naive) implementation in 1.4.
        """
        sorted_versions = ['1532-44349', '1534-44658', '1536-44582', '1536-44935', '1538-44874', '1538-44920']
        random_versions = ['1534-44658', '1536-44935', '1532-44349', '1538-44920', '1536-44582', '1538-44874']
        assert sorted_versions == natsort(random_versions)

    def test_input_order_irrelevant(self):
        """
        Test that order of input does not adversely affect order of output.

        Works by shuffling the input and checking that all 10.000 iterations
        result in the same output.
        """
        sorted_strings = ['1532-44349', '1534-44658', '1536-44582', '1536-44935', '1538-44874', '1538-44920']
        mutable_copy = list(sorted_strings)
        for i in range(10000):
            random.shuffle(mutable_copy)
            assert natsort(mutable_copy) == sorted_strings

    def test_eq(self):
        """Test :func:`.NaturalOrderKey.__eq__()`."""
        # Equality comparison between objects of same type.
        assert NaturalOrderKey('1.0') == NaturalOrderKey('1.0')
        # Equality comparison between objects of different types.
        assert NaturalOrderKey('1.0').__eq__(object) is NotImplemented

    def test_ne(self):
        """Test :func:`.NaturalOrderKey.__ne__()`."""
        # Non-equality comparison between objects of same type.
        assert NaturalOrderKey('1.0') != NaturalOrderKey('1.1')
        # Non-equality comparison between objects of different types.
        assert NaturalOrderKey('1.0').__ne__(object()) is NotImplemented

    def test_lt(self):
        """Test :func:`.NaturalOrderKey.__lt__()`."""
        # Less than comparison between objects of same type.
        assert NaturalOrderKey('1') < NaturalOrderKey('1.1')
        # Less than comparison between objects of different types.
        assert NaturalOrderKey('1').__lt__(object()) is NotImplemented

    def test_le(self):
        """Test :func:`.NaturalOrderKey.__le__()`."""
        # Less than or equal comparison between objects of same type.
        assert NaturalOrderKey('1') <= NaturalOrderKey('1.1')
        assert NaturalOrderKey('1') <= NaturalOrderKey('1')
        assert not (NaturalOrderKey('1.1') <= NaturalOrderKey('1'))
        # Less than or equal comparison between objects of different types.
        assert NaturalOrderKey('1').__le__(object()) is NotImplemented

    def test_gt(self):
        """Test :func:`.NaturalOrderKey.__gt__()`."""
        # Greater than comparison between objects of same type.
        assert NaturalOrderKey('1.1') > NaturalOrderKey('1')
        # Greater than comparison between objects of different types.
        assert NaturalOrderKey('1').__gt__(object()) is NotImplemented

    def test_ge(self):
        """Test :func:`.NaturalOrderKey.__ge__()`."""
        # Greater than or equal comparison between objects of same type.
        assert NaturalOrderKey('1.1') >= NaturalOrderKey('1')
        assert NaturalOrderKey('1') >= NaturalOrderKey('1')
        assert not (NaturalOrderKey('1') >= NaturalOrderKey('1.1'))
        # Greater than or equal comparison between objects of different types.
        assert NaturalOrderKey('1').__ge__(object()) is NotImplemented


if __name__ == '__main__':
    unittest.main()
