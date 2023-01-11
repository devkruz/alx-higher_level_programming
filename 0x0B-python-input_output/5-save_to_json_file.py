#!/usr/bin/python3
""" write object to JSON file """
from json import dumps


def save_to_json_file(my_obj, filename):
    """ write object to JSON file """

    json_rep = dumps(my_obj)
    with open(filename, "w") as file:
        file.write(json_rep)
