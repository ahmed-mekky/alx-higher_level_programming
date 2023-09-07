#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    args = sys.argv

    args_len = len(args)
    x = 0
    if args_len < 2:
        print("0")
    elif args_len == 2:
        print("{}".format(int(args[1])))
    else:
        for i in range(1, args_len):
            x += int(args[i])
        print("{}".format(x))
