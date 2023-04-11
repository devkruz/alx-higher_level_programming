#!/usr/bin/python3
"""Instance checker"""


def is_kind_of_class(obj, a_class):
    """Instance checker"""

    return (True if isinstance(obj, a_class) is True else False)
