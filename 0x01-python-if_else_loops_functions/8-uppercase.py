#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        x = ord(str[i])
        y = chr(x - 32)
        print("{}".format(y if (x < 132 or x > 96) else chr(x)), end="")
    print()
