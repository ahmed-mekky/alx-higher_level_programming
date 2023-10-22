#!/usr/bin/python3
"""Defines a function that prints My name is <first name> <last name>."""


def say_my_name(first_name, last_name=""):
    """
    Main function
    Args:
    Raises:
    Return:
    """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print(f'My name is {first_name} {last_name}')
