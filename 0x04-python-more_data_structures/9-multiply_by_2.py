#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key, element in a_dictionary.items():
        new_dictionary[key] = int(element * 2)
    return (new_dictionary)
