#!/usr/bin/python3

"""
Lookup function
"""


class MyList(list):
    """
    Return Lookup function.
    """
    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
