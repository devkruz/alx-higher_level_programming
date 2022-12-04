#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse = sorted(my_list, reverse=True)

    for num in reverse:
        print("{:d}".format(num))
