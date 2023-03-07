#!/usr/bin/python3

alt = 1
for i in range(122, 96, -1):
    if alt % 2 == 0:
        i = i - 32
    alt += 1
    print("{:c}".format(i), end="")
