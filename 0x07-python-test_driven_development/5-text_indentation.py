#!/usr/bin/python3
""" a program that prints a text with 2 new lines after each of these characters: ., ? and :
with tests
"""


def text_indentation(text):
    """ a function that prints a text with 2 new lines after each of these characters: ., ? and : """
    char = 0
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    while (char < len(text)):
        print(text[char], end="")
        if (text[char] == "?" or text[char] == "." or text[char] == ":"):
            print("\n")
            j = char
            while (text[j] == " "):
                j += 1
            char += char - j + 1
        char += 1

