#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
result = "0"
if number < 0:
    digit = (((number * -1) % 10) * -1)
else:
    digit = number % 10
if digit < 6 and digit != 0:
    result = "less than 6 and not 0"
elif digit > 5:
    result = "greater than 5"
print(f"Last digit of {number} is {digit} and is {result}")
