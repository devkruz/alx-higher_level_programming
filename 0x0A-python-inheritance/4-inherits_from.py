#!/usr/bin/python3
"""Inheritance checker"""


def inherits_from(obj, a_class):
    """Inheritance checker"""

    return (True if issubclass(type(obj), a_class) is True and type(obj) != a_class  else False)
