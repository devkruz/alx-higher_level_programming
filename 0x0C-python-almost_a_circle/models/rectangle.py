#!/usr/bin/python3
""" Rectangle class definaton """
from models.base import Base


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
        super().__init__(id)

    @property
    def width(self):
        """ set/get the width of instance """
        return self.__width

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
        return self.__height

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
        return self.__x

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
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("{} must be an integer".format("y"))
        if y < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = y

    def area(self):
        """ get the area of the instance """
        return self.__width * self.__height

    def display(self):
        """ print the instance with # char """
        length = self.height
        breath = self.width
        x = self.x
        y = self.y

        for tmp in range(y):
            print("")
        for tmp in range(length):
            for tmp in range(x):
                print(" ", end="")
            for tmp in range(breath):
                print("#", end="")
            print()

    def update(self, *args):
        """ updates the instance attributes
            args:
                args[0](int) - id
                args[1](int) - width
                args[2](int) - height
                args[3](int) - x
                args[4](int) - y
         """
        try:
            id = args[0]
            super().__init__(id)
        except IndexError:
            pass
        try:
            width = args[1]
            if not isinstance(width, int):
                raise TypeError("{} must be an integer".format("width"))
            if width <= 0:
                raise ValueError("{} must be > 0".format("width"))
            self.width = width
        except IndexError:
            pass
        try:
            height = args[2]
            if not isinstance(height, int):
                raise TypeError("{} must be an integer".format("height"))
            if height <= 0:
                raise ValueError("{} must be > 0".format("height"))
            self.height = height
        except IndexError:
            pass
        try:
            x = args[3]
            if not isinstance(x, int):
                raise TypeError("{} must be an integer".format("x"))
            if x < 0:
                raise ValueError("{} must be >= 0".format("x"))
            self.x = x
        except IndexError:
            pass
        try:
            y = args[4]
            if not isinstance(y, int):
                raise TypeError("{} must be an integer".format("y"))
            if y < 0:
                raise ValueError("{} must be >= 0".format("y"))
            self.y = y
        except IndexError:
            pass

    def to_dictionary(self):
        """ Dictionary representation of instance """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """ Instance representation """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)
