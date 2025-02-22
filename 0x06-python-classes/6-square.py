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

        if (not isinstance(self.__position, tuple) or
                len(self.__position) != 2 or
                not isinstance(self.__position[0], int) or
                not isinstance(self.__position[1], int) or
                not self.__position[0] >= 0 or
                not self.__position[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """ retrieve size """
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                not value[0] >= 0 or
                not value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ prints square """
        if (self.size == 0):
            print("")
        else:
            [print("") for i in range(self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for j in range(self.__position[0])]
                [print("#", end="") for k in range(self.__size)]
                print("")
