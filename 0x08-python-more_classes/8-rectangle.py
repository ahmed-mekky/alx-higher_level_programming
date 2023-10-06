#!/usr/bin/python3
"""python more OOP"""


class Rectangle:
    """class rectangle"""

    number_of_instances = 0
    print_symbol = []

    def __init__(self, width=0, height=0):
        """initialise the class with attributes of a rectangle."""
        a = Rectangle.print_symbol
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = a if a != [] else "#"

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

    @property
    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        var = ""
        a = self.print_symbol
        b = self.width
        c = self.height
        if self.width <= 0 or self.height <= 0:
            return var
        for i in range(self.height):
            var += f"{a}" * b + ('\n' if i < c - 1 else "")
        return var

    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area < rect_2.area:
            return rect_2
        else:
            return rect_1
