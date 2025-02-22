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
