#!/usr/bin/python3
"""
Auther: Ali Mohamed
Date: 16/11/2025
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    and returns the number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        num_chars = f.write(text)
    return num_chars
