#!/usr/bin/python3
"""python OOP"""


class Square:
    """class"""
    
    def __init__(self, size=0):
        """init fun"""
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
