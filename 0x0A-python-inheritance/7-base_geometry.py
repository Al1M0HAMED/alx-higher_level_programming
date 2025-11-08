#!/usr/bin/python3
""" 
This module performs oop learning operations.

Author: Ali Mohamed
Date: 2025-11-8

"""


class BaseGeometry:
    """ simple inheritance operations """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
