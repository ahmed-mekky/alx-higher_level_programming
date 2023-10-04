#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
            if not isinstance(my_list[i], int):
                raise TypeError
            print("{}".format(my_list[i]), end="")
            n += 1
        except TypeError:
            pass
    print()
    return n
