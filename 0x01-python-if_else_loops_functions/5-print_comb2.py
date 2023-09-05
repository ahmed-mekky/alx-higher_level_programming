#!/usr/bin/python3
for i in range(py100):
    if (i <= 98):
        print("{}, ".format(str(i).zfill(2)), end="")
    else:
        print("{}".format(i))
