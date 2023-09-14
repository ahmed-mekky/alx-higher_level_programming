#!/usr/bin/python3
def best_score(a_dictionary):
    new_dict = a_dictionary
    for item, value in a_dictionary:
        item = value **2
    return new_dict
