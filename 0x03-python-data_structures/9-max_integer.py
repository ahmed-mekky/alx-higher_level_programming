#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = None if not my_list else 0
    for i in range(len(my_list)):
        if my_list[i] > max_int:
            max_int = int(my_list[i])
    return max_int
