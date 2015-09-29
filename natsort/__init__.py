# Simple natural order sorting API for Python.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: September 29, 2015
# URL: https://github.com/xolox/python-naturalsort

"""Simple natural order sorting API for Python."""

# Standard library modules.
import re

__version__ = '1.5'
"""Semi-standard module versioning."""

integer_pattern = re.compile('([0-9]+)')
"""Compiled regular expression to match a consecutive run of digits."""

integer_type = int
"""The type used to coerce strings of digits into Python numbers."""


def natsort(l, key=None, reverse=False):
    """
    Sort the given list in the way that humans expect (using natural order sorting).

    :param l: An iterable of strings to sort.
    :param key: An optional sort key similar to the one accepted by Python's
                built in :func:`sorted()` function. Expected to produce
                strings.
    :param reverse: Whether to reverse the resulting sorted list.
    :returns: A sorted list of strings.
    """
    return sorted(l, key=lambda v: NaturalOrderKey(key and key(v) or v), reverse=reverse)


def natsort_key(s):
    """
    Turn a string into a list of substrings and numbers.

    :param s: The string to split.
    :returns: A list of strings and/or integers.
    """
    return [coerce(c) for c in integer_pattern.split(s) if c != '']


def coerce(s):
    """
    Coerce strings of digits into proper integers.

    :param s: A string.
    :returns: An integer (if coercion is possible) or the original string.
    """
    if s.isdigit():
        return integer_type(s)
    else:
        return s


class NaturalOrderKey(object):

    """
    Rich comparison for natural order sorting keys.

    This class implements rich comparison operators for natural order sorting
    that is compatible with both Python 2 and Python 3.

    Previous versions of the `naturalsort` package directly compared the
    iterables produced by :func:`natsort_key()` however in Python 3 this can
    raise :exc:`~exceptions.TypeError` due to comparisons between integers and
    strings (which Python 3 does not allow).
    """

    def __init__(self, value):
        """
        Initialize a :class:`NaturalOrderKey` object.

        :param value: A string given to :func:`natsort_key()` to get the
                      natural order sorting key used in the rich comparison
                      methods implemented by this class.
        """
        self.key = natsort_key(value)

    def __eq__(self, other):
        """Equality comparison for natural order sorting keys."""
        if isinstance(other, self.__class__):
            return self.key == other.key
        else:
            return NotImplemented

    def __ne__(self, other):
        """Non equality comparison for natural order sorting keys."""
        if isinstance(other, self.__class__):
            return self.key != other.key
        else:
            return NotImplemented

    def __lt__(self, other):
        """Less than comparison for natural order sorting keys."""
        if isinstance(other, self.__class__):
            for i, j in zip(self.key, other.key):
                if i != j:
                    if not isinstance(i, integer_type) or not isinstance(j, integer_type):
                        # Comparisons between two integers are safe but
                        # otherwise we fall back to a string comparison
                        # to avoid type errors raised by Python 3.
                        i = str(i)
                        j = str(j)
                    if i < j:
                        return True
                    if i > j:
                        return False
            return False
        else:
            return NotImplemented

    def __le__(self, other):
        """Less than or equal comparison for natural order sorting keys."""
        if isinstance(other, self.__class__):
            return self < other or self == other
        else:
            return NotImplemented

    def __gt__(self, other):
        """Greater than comparison for natural order sorting keys."""
        return not (self <= other)

    def __ge__(self, other):
        """Greater than or equal comparison for natural order sorting keys."""
        if isinstance(other, self.__class__):
            return self > other or self == other
        else:
            return NotImplemented
