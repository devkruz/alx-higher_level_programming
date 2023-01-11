#!/usr/bin/python3
""" JSON repersentation of an object """
from json import dumps


def to_json_string(my_obj):
    """ JSON representation of an object """

    return (dumps(my_obj, sort_keys=True))
