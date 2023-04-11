#!/usr/bin/python3
""" Mylist class """


class MyList(list):
    """list class child"""
    def __init__(self):
        """object initialization"""
        super().__init__(self)

    def print_sorted(self):
        """print the sorted list object"""
        print(sorted(self))
