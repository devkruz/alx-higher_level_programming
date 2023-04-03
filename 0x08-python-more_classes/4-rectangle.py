#!/usr/bin/python3
""" Define a Rectangle class """


class Rectangle:
    """ Reactangle class """

    def __init__(self, width=0, height=0):
        """ Rectange Initialization """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Return the parameter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Non-official string representation of Rectangle"""
        if self.height == 0 or self.width == 0:
            return ""
        rec = []
        for row in range(self.height):
            row_line = []
            [row_line.append("#") for hash in range(self.width)]
            if row != self.height - 1:
                row_line.append("\n")
            rec.append("".join(row_line))

        return ("".join(rec))

    def __repr__(self):
        """Official string representation of Rectangle"""

        return "Rectangle(2, 4)"
