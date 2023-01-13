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
        if not isinstance(width, int):
            raise TypeError("{} must be an integer".format("width"))
        if not isinstance(height, int):
            raise TypeError("{} must be an integer".format("height"))
        if not isinstance(x, int):
            raise TypeError("{} must be an integer".format("x"))
        if not isinstance(y, int):
            raise TypeError("{} must be an integer".format("y"))
        if width <= 0:
            raise ValueError("{} must be > 0".format("width"))
        if height <= 0:
            raise ValueError("{} must be > 0".format("height"))
        if x < 0:
            raise ValueError("{} must be >= 0".format("x"))
        if y < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """ set/get the width of instance """
        return self.width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("{} must be an integer".format("width"))
        if width <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = width

    @property
    def height(self):
        """ set/get height of instance """
        return self.height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("{} must be an integer".format("height"))
        if height <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = height

    @property
    def x(self):
        """ set/get the x coordinate of instance """
        return self.x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("{} must be an integer".format("x"))
        if x < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = x

    @property
    def y(self):
        """ set/get the y coordinate of instance """
        return self.y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("{} must be an integer".format("y"))
        if y < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = y
