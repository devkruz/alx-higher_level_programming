#!/usr/bin/python3
""" print the content of a text file """


def read_file(filename=""):
    """ print the content of a text file """

    with open(filename) as file:
        print(file.read(), end="")
