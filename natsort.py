# Simple natural order sorting API for Python that just works.
#
# Author: Peter Odding <peter.odding@paylogic.eu>
# Last Change: July 6, 2013
# URL: https://wiki.paylogic.eu/ItTools

# Standard library modules.
import re

# Regular expression to match a consecutive run of digits.
integer_pattern = re.compile('([0-9]+)')

# Regular expression to match what looks like a filename extension.
filename_extension_pattern = re.compile(r'(\.tar\.\w+|\.\w+)$')

def natsort(l, key=None):
    """
    Sort the given list in the way that humans expect (using natural order
    sorting).
    """
    return sorted(l, key=lambda v: natsort_key(key and key(v) or v))

def natsort_key(s):
    """
    Turn a string into a list of substrings and numbers that can be used as a
    sorting key. This is somewhat specialized towards sorting of filenames with
    version numbers in them; it strips and ignores (what look like) filename
    extensions.
    """
    s = filename_extension_pattern.sub('', s)
    return [coerce(c) for c in integer_pattern.split(s) if c != '']

def coerce(s):
    """
    Coerce strings of digits into proper integers.
    """
    if s.isdigit():
        return int(s)
    else:
        return s
