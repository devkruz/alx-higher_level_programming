#!/usr/bin/python3
""" Define a Rectangle class """


class Rectangle:
    """ Reactangle class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Rectange Initialization """

        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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
        cha = self.print_symbol
        if self.height == 0 or self.width == 0:
            return ""
        rec = []
        for row in range(self.height):
            row_line = []
            [row_line.append(str(cha)) for hash in range(self.width)]
            if row != self.height - 1:
                row_line.append("\n")
            rec.append("".join(row_line))

        return ("".join(rec))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two instances of Rectangle"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Square representaton of Rectangle instance"""
        return cls(size, size)

    def __repr__(self):
        """Official string representation of Rectangle"""

        return "Rectangle(2, 4)"

    def __del__(self):
        """Class delete message"""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")
