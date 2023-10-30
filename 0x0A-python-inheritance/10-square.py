#!/usr/bin/python3
"""Inheritance Modules"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """This thing adds something to the world."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
