#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Rectangle class initialization"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """Calculated the area of the rectangle"""
        return (self.__height * self.__width)

    def __str__(self):
        """String representation of Rectangle"""
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__width, self.__height))
