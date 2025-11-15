#!/usr/bin/python3
"""
Auther: Ali Mohamed
Date: 16/11/2025
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    print (content, end="")
