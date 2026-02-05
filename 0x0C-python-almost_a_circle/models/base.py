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

    @classmethod
    def create(cls, **dictionary):
        """
        creats an instance
        """
        if dictionary and len(dictionary) > 0:
            obj = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
            obj.update(**dictionary)
            return (obj)

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        dict to json
        """
        if list_dictionaries is not None and len(list_dictionaries) >= 1:
            return (json.dumps(list_dictionaries))
        else:
            return ("[]")

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save to a file
        """
        filename = f"{cls.__name__}.json"
        if list_objs is not None and len(list_objs) >= 1:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        else:
            list_dicts = []
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        to dict
        """
        if json_string is None or len(json_string) < 1:
            return ([])
        else:
            dict_list = json.loads(json_string)
            return (dict_list)
