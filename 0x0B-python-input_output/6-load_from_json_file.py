#!/usr/bin/python3
""" create python object from a json file """
from json import loads


def load_from_json_file(filename):
    """ create from a json file """

    with open(filename, "r") as file:
        json_rep = file.read()
        return (loads(json_rep))
