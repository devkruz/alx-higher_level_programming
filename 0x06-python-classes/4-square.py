#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class defination"""

    def __init__(self, size=0) -> None:
        """Initialize a new instance

            Args:
                size: The size of the square instance
        """
        self.size = size

    @property
    def size(self):
        """size attribute: getter"""

        return self.__size

    @size.setter
    def size(self, value):
        """size attribute: setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square instance"""

        return (self.__size * self.__size)
