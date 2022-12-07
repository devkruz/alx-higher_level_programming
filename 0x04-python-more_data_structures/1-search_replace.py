#!/usr/bin/python3

def search_replace(my_list, search, replace):
    list_copy = my_list[:]
    all = list_copy.count(search)

    while all:
        index = list_copy.index(search)
        list_copy[index] = replace
        all = list_copy.count(search)

    return list_copy
