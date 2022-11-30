#!/usr/bin/python3

def uppercase(str):
    for char in range(len(str)):
        shift = 0
        if (ord(str[char]) >= 97) and (ord(str[char]) <= 122):
            shift = 32
        print("{:c}".format(ord(str[char]) - shift), end="")
    print("")
