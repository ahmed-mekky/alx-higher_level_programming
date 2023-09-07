#!/usr/bin/python3
import calculator_1 as cc
if __name__ == '__main__':
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, cc.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, cc.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, cc.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, cc.div(a, b)))
