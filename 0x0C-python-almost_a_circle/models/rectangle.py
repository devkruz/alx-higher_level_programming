#!/usr/bin/python3
""" Rectangle class definaton """
from base import Base


class Rectangle(Base):
    """
    Rectangle class definaton

    args:
        width(int): width of the instance
        height(int): height of the instance
        x(int): x coordinate of the instance
        y(int): y coordinate of the instance
        id(int): the instance identity

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle Instance Initialization """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, y):
        self.__y = y
