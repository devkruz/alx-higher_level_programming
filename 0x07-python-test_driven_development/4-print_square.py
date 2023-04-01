#!/usr/bin/python3
"""Define print_square"""


def print_square(size):
    """Print a square with the character #"""

    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        for hash in range(size):
            print("#", end="")
        print("")
