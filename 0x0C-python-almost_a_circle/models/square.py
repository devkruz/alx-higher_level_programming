#!/usr/bin/python3
""" square class definaton """
from rectangle import Rectangle


class Square(Rectangle):
    """
    square class defination
    args:
        size(int): width and height of instance
        x(int): x coordinate of the instance
        y(int): y coordinate of the instance
        id(int): the instance identity

    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Instance initialization """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """ get/set instance width and height """
        return self.width

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("{} must be an integer".format("width"))
        if size <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.width = size
        self.height = size

    def update(self, *args):
        """ updates the instance attributes
            args:
                args[0](int) - id
                args[1](int) - size
                args[2](int) - x
                args[3](int) - y
         """
        try:
            id = args[0]
            super().__init__(width=self.width, height=self.height, id=id)
        except IndexError:
            pass
        try:
            size = args[1]
            if not isinstance(size, int):
                raise TypeError("{} must be an integer".format("width"))
            if size <= 0:
                raise ValueError("{} must be > 0".format("width"))
            self.size = size
        except IndexError:
            pass
        try:
            x = args[2]
            if not isinstance(x, int):
                raise TypeError("{} must be an integer".format("x"))
            if x < 0:
                raise ValueError("{} must be >= 0".format("x"))
            self.x = x
        except IndexError:
            pass
        try:
            y = args[3]
            if not isinstance(y, int):
                raise TypeError("{} must be an integer".format("y"))
            if y < 0:
                raise ValueError("{} must be >= 0".format("y"))
            self.y = y
        except IndexError:
            pass

    def __str__(self):
        """ Instance representation """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)
