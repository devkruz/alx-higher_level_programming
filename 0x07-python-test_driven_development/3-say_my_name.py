#!/usr/bin/python3
"""Define say_my_name"""


def say_my_name(first_name, last_name=""):
    """Print the name in the parameter"""

    if isinstance(first_name, str) == False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) == False:
        raise TypeError("last_name must be a string")
    intro = "My name is {} {}"
    print(intro.format(first_name, last_name))
