#!/usr/bin/python3
"""Student class"""


class Student():
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Student class initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dictionary representation this instance"""
        return self.__dict__
