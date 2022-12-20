#!/usr/bin/python3

def best_score(a_dictionary):

    if isinstance(a_dictionary, dict) and len(a_dictionary) > 0:
        max_key = list(a_dictionary.keys())[0]
        max_value = a_dictionary[max_key]

        for key, value in a_dictionary.items():
            if value > max_value:
                max_value = value
                max_key = key

        return max_key
    else:
        return "None"



a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))