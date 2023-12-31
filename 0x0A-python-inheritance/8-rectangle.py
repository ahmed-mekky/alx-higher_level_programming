#!/usr/bin/python3
"""Inheritance Modules"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This thing adds something to the world."""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
