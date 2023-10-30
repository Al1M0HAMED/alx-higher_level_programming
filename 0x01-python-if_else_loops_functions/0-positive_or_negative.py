#!/usr/bin/python3
import random
number = random.randint(-10, 10)
result = "is negative"
if number == 0:
    result = "is zero"
elif number > 0:
    result = "is positive"
print(f"{number} {result}")
