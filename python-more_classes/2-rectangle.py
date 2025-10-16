#!/usr/bin/python3
"""
Calculate Rectangle
"""


class Rectangle:
    """
    Rectangle Class.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # GETTER METHOD
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    # SETTER METHOD
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

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
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2
