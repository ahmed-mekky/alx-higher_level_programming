#!/usr/bin/python3
"""python more OOP"""


class Rectangle:
    """class rectangle"""

    def __init__(self, width=0, height=0):
        """initialise the class with attributes of a rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        var = ""
        if self.width <= 0 or self.height <= 0:
            return var
        for i in range(self.height):
            var += "#" * self.width + ('\n' if i < self.height - 1 else "")
        return var

    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")
