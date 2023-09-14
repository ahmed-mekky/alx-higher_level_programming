#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if my_list[i] == search:
            new_list[i] = replace
        elif my_list[i] == replace:
            new_list[i] = search
        else:
            new_list[i] = my_list[i]
    return new_list
