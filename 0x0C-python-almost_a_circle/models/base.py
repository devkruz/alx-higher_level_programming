#!/usr/bin/python3
""" Base class defination """
from json import dumps, loads


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON string representation of a list dictionary
        args:
            list_dictionaries: list dictionary

        """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save JSON string representation to a file
        args:
            list_objs: list dictionary

        """
        file = cls.__name__ + ".json"
        with open(file, "w") as jfile:
            if list_objs is None or\
             list_objs == []:
                jfile.write("[]")
            else:
                to_dic = [obj.to_dictionary() for obj in list_objs]
                jfile.write(Base.to_json_string(to_dic))

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """
        if json_string is None or json_string == "":
            return {}
        else:
            return loads(json_string)
