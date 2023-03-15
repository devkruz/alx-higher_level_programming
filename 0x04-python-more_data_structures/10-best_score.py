#!/usr/bin/python3

def best_score(a_dictionary):

    if type(a_dictionary) is not dict or len(a_dictionary) == 0:
        return "None"
    else:
        max_key, max_value = list(a_dictionary.items())[0]

        for key, value in a_dictionary.items():
            if value > max_value:
                max_value = value
                max_key = key

        return max_key
