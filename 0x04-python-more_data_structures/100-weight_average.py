#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    size = 0
    weight = 0

    for tuple in my_list:
        weight += (tuple[0] * tuple[1])
        size += tuple[1]

    return (weight / size)
