#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__("7-base_geometry")


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Rectangle class initialization"""
        BaseGeometry.interger_validator("width", width)
        BaseGeometry.interger_validator("height", height)
        self.__height = height
        self.__width = width
