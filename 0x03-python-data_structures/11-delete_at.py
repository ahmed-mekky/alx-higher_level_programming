#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in range(len(my_list)):
        if i is idx:
            my_list[i:i+1] = []
    return my_list
