#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    new_list = list(sorted(a_dictionary.values()))
    for key, value in a_dictionary.items():
        if (value == new_list[-1]):
            elkey = key
    return elkey
