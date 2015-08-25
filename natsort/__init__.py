# Simple natural order sorting API for Python.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: August 25, 2015
# URL: https://github.com/xolox/python-naturalsort

"""Simple natural order sorting API for Python."""

# Standard library modules.
import re

# Semi-standard module versioning.
__version__ = '1.3'

# Regular expression to match a consecutive run of digits.
integer_pattern = re.compile('([0-9]+)')


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
    return sorted(l, key=lambda v: natsort_key(key and key(v) or v),
                  reverse=reverse)


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
        return int(s)
    else:
        return s
