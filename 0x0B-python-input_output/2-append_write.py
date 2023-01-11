#!/usr/bin/python3
""" write/append to a file """


def append_write(filename="", text=""):
    """ write/append to a file """

    with open(filename, "a") as file:
        return(file.write(text))
