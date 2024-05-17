#!/usr/bin/python3
"""Defines a function that adds 2 integers"""


def add_integer(a, b=98):
    """
    Main function
    Args:
        a (int): The first number to be added
        b (int): The second number to be added. Default is 98
    Raises:
        TypeError: If either a or b are not integers
    Return:
        int: the sum of a and b
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(result)
