#!/usr/bin/python3
"""
Base class
"""
import json


class Base:
    """
    base class
    """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        dict to json
        """
        if list_dictionaries is not None and len(list_dictionaries) >= 1:
            return (json.dumps(list_dictionaries))
        else:
            return ("[]")
