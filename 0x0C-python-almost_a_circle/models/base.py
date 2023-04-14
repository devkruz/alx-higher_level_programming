#!/usr/bin/python3
""" Base class defination """
from json import dumps, loads
import csv


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
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save JSON string representation of a
        object to a file
        args:
            list_objs: list of instance

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
            return []
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create a new instance
            args:
                dictionary: dictionary containing instance attribute
        """
        if cls.__name__ == "Rectangle":
            new_rec = cls(2, 2)
        else:
            new_rec = cls(2)

        new_rec.update(**dictionary)
        return new_rec

    @classmethod
    def load_from_file(cls):
        """Load instances from json file

            returns: list of instance if json file
            equivalent to the class name exit else
            empty list
        """
        file = cls.__name__ + ".json"
        try:
            with open(file) as jfile:
                json_string = jfile.read()
                dic_list = cls.from_json_string(json_string)
                obj_list = [cls.create(**each_dic) for each_dic in dic_list]

                return obj_list
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save CSV representation of an object to a file"""
        file = cls.__name__ + ".csv"
        with open(file, mode="w") as cvsfile:
            if list_objs is None or\
                    list_objs == []:
                cvsfile.write("[]")
            else:
                table = list_objs[0].to_dictionary().keys()
                dic_writer = csv.DictWriter(cvsfile, fieldnames=table)
                dic_writer.writeheader()
                for objs in list_objs:
                    dic_writer.writerow(objs.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Load instance from a CSV file"""
        file = cls.__name__ + ".csv"
        with open(file) as csvfile:
            dic_reader = csv.DictReader(csvfile)
            obj_list = [dict([k, int(v)] for k, v in each_dic.items())
                        for each_dic in dic_reader]
            return obj_list
