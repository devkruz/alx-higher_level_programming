#!/usr/bin/python3
""" python object from a JSON representation """
from json import loads


def from_json_string(my_str):
    """ python object from a JSON representation """
    return (loads(my_str))
