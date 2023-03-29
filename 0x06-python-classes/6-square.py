#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class defination"""

    def __init__(self, size=0, position=(0, 0)) -> None:
        """Initialize a new instance

            Args:
                size: The size of the square instance
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size attribute: getter"""

        return self.__size

    @size.setter
    def size(self, value):
        """Size attribute: setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position attribute: getter"""

        return self.__position

    @position.setter
    def position(self, value):
        """Position attribute: setter"""

        if len(value) != 2 or type(value) != tuple or\
                type(value[0]) != int or type(value[1]) != int:
            raise ("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Area of the square instance"""

        return (self.__size * self.__size)

    def my_print(self):
        """Prints the area of the square instance"""

        if self.__size == 0:
            print("")

        for row in range(self.__size):
            [print(" ", end="") for space in range(self.position[0])]
            [print("#", end="") for hash in range(self.__size)]
            print("")
