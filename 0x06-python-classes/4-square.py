#!/usr/bin/python3
"""python OOP"""


class Square:
    """class"""
    def __init__(self, size=0):
        """init fun"""
        self.__size = size

    @size.setter
    def size(self):
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        

    @property
    def size(self):
        return (self.__size)

    def area(self):
        return (self.__size ** 2)
