#!/usr/bin/python3
"""
Inheritance Modules
"""


def inherits_from(obj, a_class):
    """
    This thing adds something to the world.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
