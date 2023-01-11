#!/usr/bin/python3
""" write a string to a text file """


def write_file(filename="", text=""):
    """ write a string to a text file """

    with open(filename, "w") as file:
        return(file.write(text))
