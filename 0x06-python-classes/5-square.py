#!/usr/bin/python3
"""python OOP"""


class Square:
    """class"""
    def __init__(self, size=0):
        """init fun"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)
    
    def my_print(self):
        i = self.__size
        if self.__size == 0:
            print()
        while i > 0:
            j = self.__size
            while j > 0:
                print('#', end="")
                j -= 1
            print()
            i -= 1
