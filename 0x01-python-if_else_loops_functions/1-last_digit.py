#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = (((number * -1) % 10) * -1)
else:
    last_digit = (number % 10)

if last_digit > 5:
    digit_status = "and is greater than 5"
elif last_digit < 6 and last_digit != 0:
    digit_status = "and is less than 6 and not 0"
else:
    digit_status = "and is 0"

print(f"Last digit of {number} is {last_digit} {digit_status}")
