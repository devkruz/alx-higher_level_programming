#!/usr/bin/python3
"""Strict Instance checker"""


def is_same_class(obj, a_class):
    """Strict Instace checker"""

    return(True if type(obj) == a_class else False)
