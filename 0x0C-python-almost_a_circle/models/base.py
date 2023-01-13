#!/usr/bin/python3
""" Base class defination """


class Base:
    """
    Base - The base class of every other
    class in this project

    Priviate class attribute:
    __nb_objects: number of instance initialized

     """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Instance initialization
        args:
            id(int): Instance id
         """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
