#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    result = 0
    rest = 0
    for i in range(len(my_list)):
        result += my_list[i][0] * my_list[i][1]
        rest += my_list[i][1]
    return (result / rest)
