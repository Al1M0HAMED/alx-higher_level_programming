#!/usr/bin/python3
"""
student class
"""


class Student:
    """
    student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        all_strings = True
        if attrs is not None:
            for item in attrs:
                if not isinstance(item, str):
                    all_strings = False
                    break
        if all_strings is True and attrs is not None:
            filtered_dict = {}
            i = 0
            while i < len(attrs):
                key = attrs[i]
                if key in self.__dict__:
                    filtered_dict[key] = self.__dict__[key]
                i += 1
            return (filtered_dict)
        else:
            return (self.__dict__)
