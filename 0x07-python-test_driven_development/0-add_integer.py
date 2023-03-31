#!/usr/bin/python3
"""Define add_integer"""


def add_integer(a, b=98):
    """Add two interger"""

    if isinstance(a, int) == False and isinstance(a, float) == False:
        raise TypeError("a must be an integer")
    if isinstance(b, int) == False and isinstance(b, float) == False:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
