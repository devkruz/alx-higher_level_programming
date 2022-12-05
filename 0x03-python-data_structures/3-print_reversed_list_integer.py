#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        my_list = sorted(my_list, reverse=True)
        for num in my_list:
            print("{:d}".format(num))
