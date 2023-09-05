#!/usr/bin/python3
import random
number = random.randint(-10, 10)
status = "is zero"
if number > 0:
    status = "is positive"
elif number < 0:
    status = "is negative"
print(number, status)
