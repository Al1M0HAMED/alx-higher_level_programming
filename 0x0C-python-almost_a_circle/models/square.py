#!/usr/bin/python3
"""
Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """
        update
        """
        attrs = ["id", "size", "x", "y"]
        for i, attr in enumerate(attrs):
            if i < len(args):
                setattr(self, attr, args[i])
        if (kwargs is not None) and (args is None or len(args) == 0):
            for key in ["size", "id", "x", "y"]:
                if key in kwargs:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
         square to dict
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
