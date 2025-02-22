#!/usr/bin/python3
"""
This module performs oop learning operations.

Author: Ali Mohamed
Date: 2024-02-23
"""


class Square:
    """A simple class that performs basic operations."""
    def __init__(self, size=0):
        """creates a square"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")

    def area(self):
        """returns area of square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """ retrieve size """
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
