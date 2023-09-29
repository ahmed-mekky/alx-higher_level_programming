#!/usr/bin/python3
"""python OOP"""


class Square:
    """class"""
    def __init__(self, size=0):
        """init fun"""
        if type(size) is not int:
            print("Size must be an integer")
        if size < 0:
            print('ValueError')
        self.__size = size
