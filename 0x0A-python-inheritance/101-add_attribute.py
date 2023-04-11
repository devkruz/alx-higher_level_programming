#!/usr/bin/python3
"""Savely add attribute"""


def add_attribute(mc, att, value):
    """Savely add attribute"""
    if not hasattr(mc, att):
        raise TypeError("can't add new attribute")
    else:
        setattr(mc, att, value)
