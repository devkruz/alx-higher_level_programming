#!/usr/bin/python3

def best_score(a_dictionary):

    if isinstance(a_dictionary, dict):
        keys = []

        for key in a_dictionary.keys():
            keys.append(key)
        max = a_dictionary[keys[0]]
        for key in keys:
            if a_dictionary[key] > max:
                max = a_dictionary[key]

        return max
    else:
        return "None"
