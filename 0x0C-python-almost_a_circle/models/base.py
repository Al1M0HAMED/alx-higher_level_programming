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

    @classmethod
    def load_from_file(cls):
        """
        loads form a json file
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                js_data = f.read()
            obj_list = cls.from_json_string(js_data)
        except FileNotFoundError:
            return ([])
        created_objects = []
        for obj in obj_list:
            created_objects.append(cls.create(**obj))
        return (created_objects)

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
