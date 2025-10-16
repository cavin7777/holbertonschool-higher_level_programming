#!/usr/bin/python3

"""
Define square empty.
"""


class Square:
    """
    Square Class.
    """

    def __init__(self, size=0):
        """function size no attribute.

        Parameters:
        size:

        Raises:
        TypeError:
        ValueError:

        """
        self.__size = size

    # getter method
    @property
    def size(self):
        return self.__size

    # setter method
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
