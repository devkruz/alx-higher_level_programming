#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = []
    for key in a_dictionary.keys():
        keys.append(key)
    keys.sort()

    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
