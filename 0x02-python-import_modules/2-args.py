#!/usr/bin/python3
import sys

args = sys.argv

args_len = len(args)

if args_len == 1:
    print("0 Arguments.")
elif args_len == 2:
    print("1 Argument:")
    print("1: {}".format(args[1]))
else:
    print("{} Arguments:".format(args_len - 1))
    for i in range(1, args_len):
        print("{}: {}".format(i, args[i]))
