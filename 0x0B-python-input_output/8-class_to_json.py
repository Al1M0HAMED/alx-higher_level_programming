#!/usr/bin/python3
"""
This module defines a function to convert a class instance
into a dictionary representation suitable for JSON serialization.
"""


def class_to_json(obj):
    return (obj.__dict__)
