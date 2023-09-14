#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    i = 0
    biggest_element, biggest_key = int(), str()
    for key, element in a_dictionary.items():
        if i == 0 or element > biggest_element:
            biggest_key = key
            biggest_element = element
        i += 1
    return (biggest_key)
