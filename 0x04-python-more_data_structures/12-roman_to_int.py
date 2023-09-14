#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    last_value = 0
    for num in reversed(roman_string):
        value = roman_dict[num]
        if value < last_value:
            result += value - last_value * 2
        else:
            result += value
        last_value = value
    return abs(result)
