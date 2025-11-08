#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

try:
    r = Rectangle(6, 5)
    print(r)
    print(r.area())
except Exception as e:
    print(e)
