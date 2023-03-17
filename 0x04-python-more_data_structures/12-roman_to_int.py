#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or None:
        return 0
    roman_table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    roman_int = 0
    index = 0

    while index < len(roman_string):
        sp_roman = None
        try:
            sp_roman = roman_string[index] + roman_string[index + 1]
        except IndexError:
            pass
        roman = roman_string[index]
        if sp_roman in roman_table:
            roman_int += roman_table[sp_roman]
            index += 1
        else:
            roman_int += roman_table[roman]

        index += 1

    return roman_int
