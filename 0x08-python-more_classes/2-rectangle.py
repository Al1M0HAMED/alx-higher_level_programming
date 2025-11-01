"""
This module performs oop learning operations.

Author: Ali Mohamed
Date: 2025-11-1
"""


class Rectangle:
    """A simple square class that performs basic operations."""
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
