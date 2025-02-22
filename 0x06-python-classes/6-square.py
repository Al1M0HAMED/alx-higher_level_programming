#!/usr/bin/python3
"""
This module performs oop learning operations.

Author: Ali Mohamed
Date: 2024-02-23
"""


class Square:
    """A simple class that performs basic operations."""
    def __init__(self, size=0, position=(0, 0)):
        """creates a square"""
        self.__size = size
        self.__position = position
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

    def is_valid_tuple(self, value):
        """ checks if valid tuple """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], tuple):
                if value[0] > 0 and value[1] > 0:
                    return (1)
        else:
            return (0)

    @property
    def position(self):
        """ retrieve size """
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets position"""
        if is_valid_tuple(value):
            self.__value = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """ prints square """
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for i in range(self.position[0]):
                    print(" ", end="")
                for i in range(self.size):
                    print("#", end="")
                print("")
