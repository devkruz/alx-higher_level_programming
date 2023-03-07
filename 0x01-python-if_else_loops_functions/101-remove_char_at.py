#!/usr/bin/python3

def remove_char_at(str, n):
    new_string = ""

    for index, ch in enumerate(str):
        if n != index:
            new_string += ch

    return new_string
