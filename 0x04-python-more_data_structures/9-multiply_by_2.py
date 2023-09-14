#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary
    for item, value in new_dict.items():
        new_dict[item] = value * 2
    return new_dict
