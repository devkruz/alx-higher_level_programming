#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    while value in a_dictionary.values():

        for key, k_value in a_dictionary.items():

            if k_value == value:
                del a_dictionary[key]
                break
    return a_dictionary
