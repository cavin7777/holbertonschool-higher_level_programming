#!/usr/bin/python3

"""
Define square empty.
"""
class Square:
    """
    Square Class.
    """

    def __init__(self, size):
        """
        function size no attribute.
        """
        
        try:
            self.__size = size

        except (size < 0):
            print("size must be >= 0")
        except (size = int()):
              print("size must be an integer")
        finally:
            pass
            