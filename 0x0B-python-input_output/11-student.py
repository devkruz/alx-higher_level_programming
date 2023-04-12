#!/usr/bin/python3
"""Student class"""


class Student():
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Student class initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Dictionary representation this instance
            filtered with a list of attrs
        """
        if (type(attrs) == list) and\
                (all([True if (type(attr) == str)
                      else False for attr in attrs])):
            return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}

        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of instance"""
        for key, value in json.items():
            setattr(self, key, value)
