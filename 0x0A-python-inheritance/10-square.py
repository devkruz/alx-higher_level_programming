#!/usr/bin/python3
"""Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Square class initialization"""
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size


s = Square(13)

print(s)
print(s.area())

