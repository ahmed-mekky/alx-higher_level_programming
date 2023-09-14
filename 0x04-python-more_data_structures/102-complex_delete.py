#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        keys = []
        for key, values in a_dictionary.items():
            if values == value:
                keys.append(key)
        for key in keys:
            del a_dictionary[key]
    return a_dictionary
