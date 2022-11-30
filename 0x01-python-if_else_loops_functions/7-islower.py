#!/usr/bin/python3

def islower(c):
    for char in range(97, 122):
        if ord(c) == char:
            return True
    return False
