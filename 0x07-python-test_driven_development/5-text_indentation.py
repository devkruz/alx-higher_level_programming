#!/usr/bin/python3
"""Define text_indentation"""


def text_indentation(text):
    """ Prints a text with 2 new lines after
        each of these characters:
         ., ? and :
    """

    if isinstance(text, str) is False:
        raise ("text must be a string")

    for cha in range(len(text)):
        if text[cha] == '.' or text[cha] == ',' or text[cha] == '/' or\
              text[cha] == ':':
            print("")
            print("")
        elif (text[cha] == " ") and\
                (text[cha - 1] == '.' or text[cha - 1] == ',' or
                    text[cha - 1] == '/' or text[cha - 1] == ':'):
            pass
        else:
            print(text[cha], end="")
