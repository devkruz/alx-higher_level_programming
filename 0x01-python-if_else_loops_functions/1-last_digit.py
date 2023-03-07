#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = -1 if number < 0 else 1
last = str(number)[-1:]
last = int(last) * sign
print(f"Last digit of {number} is {last} and is ", end="")

if last > 5:
    print("greater than 5")
elif last == 0:
    print("0")
elif last < 6 and last != 0:
    print("less than 6 and not 0")
