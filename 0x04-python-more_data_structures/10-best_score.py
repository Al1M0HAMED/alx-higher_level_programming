#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    biggest_element, biggest_key = int(), str()
    for key, element in a_dictionary.items():
        if element > biggest_element:
            biggest_key = key
            biggest_element = element
    return (biggest_key)
