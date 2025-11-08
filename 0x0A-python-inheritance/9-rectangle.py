#!/usr/bin/python3
"""
This module performs oop learning operations.

Author: Ali Mohamed
Date: 2025-11-1
"""


class Rectangle:
    """A simple square class that performs basic operations."""
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ creates a square """
        self.__width = width
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        else:
            if width < 0:
                raise ValueError("width must be >= 0")
        self.__height = height
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        else:
            if height < 0:
                raise ValueError("height must be >= 0")
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ retrieve width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """" set width value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ retrieve height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """" set height value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ retrieve area """
        return (self.__height * self.__width)

    def perimeter(self):
        """ retrieve perimeter """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height + self.__width) * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (rect_1.area() == rect_2.area()) or (rect_1.area() > rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    def __str__(self):
        rect_str = ""
        if self.__height != 0 or self.__width != 0:
            for i in range(self.__height):
                if i > 0:
                    rect_str += "\n"
                for j in range(self.__width):
                    rect_str += str(self.print_symbol)
        return (rect_str)

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
