#!/usr/bin/python3
"""Define text_indentation"""


def text_indentation(text):
    """ Prints a text with 2 new lines after
        each of these characters:
         ., ? and :
    """

    if isinstance(text, str) is False:
        raise ("text must be a string")

    for cha in text:
        if cha == '.' or ',' or '/' or ':':
            print("")
            print("")
        else:
            print(cha)
