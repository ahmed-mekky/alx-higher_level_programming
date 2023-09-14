#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    old_set = set_1.difference(set_2)
    new_set = set_2.difference(set_1)
    return old_set.union(new_set)
