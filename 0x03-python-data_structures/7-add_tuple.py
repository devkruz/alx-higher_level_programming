#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """ Add two tuple """
    new_tuple_a, new_tuple_b = check_tuble(tuple_a, tuple_b)
    a = new_tuple_a[0] + new_tuple_b[0]
    b = new_tuple_a[1] + new_tuple_b[1]
    c = a, b
    return c


def check_tuble(a=(), b=()):
    """ make tuples of length two """
    new_tuple_b = b
    new_tuple_a = a

    if len(new_tuple_a) < 2:
        if len(new_tuple_a) == 1:
            new_tuple_a = new_tuple_a[0], 0
        else:
            new_tuple_a = 0, 0
    if len(new_tuple_b) < 2:
        if len(new_tuple_b) == 1:
            new_tuple_b = new_tuple_b[0], 0
        else:
            new_tuple_b = 0, 0
    return new_tuple_a, new_tuple_b
