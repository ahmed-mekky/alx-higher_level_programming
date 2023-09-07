import sys

args = sys.argv

len = len(args)

if len == 1:
    print("0 Arguments.")
elif len == 2:
    print("1 Argument.")
    print("1: {}".format[args[1]])
else
    print("{} Arguments.".format(len - 1))
    for i in range(1, len):
        print("{}: {}".format(i, args[i]))
