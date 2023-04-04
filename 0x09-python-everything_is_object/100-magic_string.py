#!/usr/bin/python3
"""Magic string"""


def magic_string():
    """Magic string"""
    magic_string.called = getattr(magic_string, "called", 0) + 1

    return ("BestSchool" + ", BestSchool" * (magic_string.called - 1))
