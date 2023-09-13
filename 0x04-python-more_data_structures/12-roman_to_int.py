#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None and roman_string != str(roman_string):
        return (0)
    roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
    }
    previos, roman_sum = 0, 0
    for char in roman_string:
        current = roman_numerals.get(char)
        if (current is not None):
            if previos >= current:
                roman_sum += current
            else:
                roman_sum -= previos
                roman_sum += (current - previos)
            previos = current
        else:
            return (0)
    return (roman_sum)
