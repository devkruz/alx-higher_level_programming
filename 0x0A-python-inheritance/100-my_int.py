#!/usr/bin/python3
"""Invert ==  and != operator"""


class MyInt(int):
    """Invert == and != operator"""
    def __eq__(self, value):
        """Overide == behavor with !="""
        return self.real != value

    def __ne__(self, value):
        """Overide != behavor with =="""
        return self.real == value
