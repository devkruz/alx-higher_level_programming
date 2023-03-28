#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class defination"""

    def __init__(self, size: int) -> None:
        """Initialize a new instance

            Args:
                size: The size of the square instance
        """
        self.__size = size
