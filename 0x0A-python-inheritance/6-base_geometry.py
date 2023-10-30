#!/usr/bin/python3
"""Inheritance Modules"""


class BaseGeometry:
    """This thing adds something to the world."""
    def area(self):
        raise Exception("area() is not implemented")
