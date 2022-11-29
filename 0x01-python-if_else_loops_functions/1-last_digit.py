#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
last = number[-1:]
print("Last digit of" + " " + number + " is " + last, end="")
print(" and is ", end="")
last = int(last)
if last > 5:
    print("greater than 5")
elif last == 0:
    print("0")
elif last < 6 and last > 0:
    print("less than 6 and not 0")
