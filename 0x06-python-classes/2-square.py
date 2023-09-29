#!/usr/bin/python3
"""python OOP"""


class Square:
    """class"""
    def __init__(self, size=0):
        """init fun
        Args:
            size (int): t.....
        Raises:
            TypeError: the size is not integer
            ValueError: the size is less than 0
        """
        if not type(size) is int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
