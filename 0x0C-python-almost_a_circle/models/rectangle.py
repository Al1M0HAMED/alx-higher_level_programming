#!/usr/bin/python3
"""
Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def display(self):
        """
        desplays the rectangle
        """
        i = 0
        while i < self.__height:
            j = 0
            while j < self.__width:
                print("#", end="")
                j += 1
            print("")
            i += 1

    def area(self):
        """
        returns area
        """
        return (self.__width * self.__height)

    def is_validated(self, value):
        """
        is valid
        """
        validation = 1
        if isinstance(value, int):
            if value <= 0:
                validation = 2
            else:
                validation = 0
        return (validation)

    def __str__(self):
        """
        str
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        valid = self.is_validated(value)
        if valid == 0:
            self.__width = value
        elif valid == 1:
            raise TypeError("width must be an integer")
        else:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        valid = self.is_validated(value)
        if valid == 0:
            self.__height = value
        elif valid == 1:
            raise TypeError("height must be an integer")
        else:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        valid = self.is_validated(value)
        if valid == 0 or value == 0:
            self.__x = value
        elif valid == 1:
            raise TypeError("x must be an integer")
        else:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        valid = self.is_validated(value)
        if valid == 0 or value == 0:
            self.__y = value
        elif valid == 1:
            raise TypeError("y must be an integer")
        else:
            raise ValueError("y must be >= 0")
