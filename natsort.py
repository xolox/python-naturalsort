# Simple natural order sorting API for Python that just works.
#
# Author: Peter Odding <peter.odding@paylogic.eu>
# Last Change: June 14, 2013
# URL: https://wiki.paylogic.eu/ItTools

# Standard library modules.
import re

# Regular expression to match a consecutive run of digits.
integer_pattern = re.compile('([0-9]+)')

def natsort(l, key=None):
    """
    Sort the given list in the way that humans expect (using natural order
    sorting).
    """
    return sorted(l, key=lambda v: natsort_key(key and key(v) or v))

def natsort_key(s):
    """
    Turn a string into a list of substrings and numbers.
    """
    return [coerce(c) for c in integer_pattern.split(s) if c != '']

def coerce(s):
    """
    Coerce strings of digits into proper integers.
    """
    if s.isdigit():
        return int(s)
    else:
        return s
