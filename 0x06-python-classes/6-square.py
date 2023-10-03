#!/usr/bin/python3
"""python OOP"""


class Square:
    """class"""
    def __init__(self, size=0, position=(0, 0)):
        """init fun"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or position[1] < 0 or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position 

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

    @property
    def position(self):
        return (self.__posision)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or value[1] < 0 or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        i = self.__size
        if self.__size == 0:
            print()
        x = self.__position[1]
        while x:
            print()
            x -= 1
        while i > 0:
            j = self.__size
            y = self.__position[0]
            while y > 0:
                print(end=" ")
                y -= 1
            while j > 0:
                print('#', end="")
                j -= 1
            print()
            i -= 1
