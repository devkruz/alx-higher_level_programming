#!/usr/bin/python3

def no_c(my_string):
    new_string = [c for c in my_string if (c != 'c') and (c != 'C')]
    return ("".join(new_string))
