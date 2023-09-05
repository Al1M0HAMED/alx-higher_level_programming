#!/usr/bin/python3
# this function prints a string in uppercase followed by a new line.

def uppercase(s):
    for char in s:
        if (ord(char) >= 97 and ord(char) <= 122):
           char = ord(char) - ord(" ")
           char = chr(char)
        print("{}".format(char), end="")
    print('')
