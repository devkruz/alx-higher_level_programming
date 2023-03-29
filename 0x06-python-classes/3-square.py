#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class defination"""

    def __init__(self, size=0) -> None:
        """Initialize a new instance

            Args:
                size: The size of the square instance
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of the square instance"""

        return (self.__size * self.__size)
