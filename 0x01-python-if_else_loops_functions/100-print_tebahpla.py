#!/usr/bin/python3
for i in range(123, 97, -1):
    print("{}".format(chr(i) if i % 2 != 0 else chr(i - 32)), end="")
