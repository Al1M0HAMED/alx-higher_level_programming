#!/usr/bin/python3
"""
date: 15/ 11 / 2025
auther: Ali Mohamed
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False."""
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
