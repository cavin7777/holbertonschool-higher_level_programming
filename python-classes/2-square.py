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

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
            