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

    def __str__(self):
        """ Instance representation """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)
