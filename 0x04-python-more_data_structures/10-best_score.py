#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    new_list = sorted(a_dictionary.keys())
    return new_list[-1]
