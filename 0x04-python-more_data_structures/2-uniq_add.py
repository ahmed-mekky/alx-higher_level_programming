#!/usr/bin/python3
def uniq_add(my_list=[]):
    checklist = []
    result = 0
    for i in range(len(my_list)):
        if my_list[i] not in checklist:
            result += my_list[i]
            checklist.append(my_list[i])
    return result
