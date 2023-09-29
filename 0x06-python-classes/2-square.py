#!/usr/bin/python3
"""python OOP"""


class Square:
    """class"""

    def __init__(self, size=0):
        """Initializes a Square instance.
        Args:
            size (int): the size of square.
        Raises:
            TypeError: the size not integer
            ValueError: the size less that 0
        """
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
