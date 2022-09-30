#!/usr/bin/python3
"""This Module is for a class Square"""


class Square:
    """This is a class that defines Square with a size"""

    def __init__(self, size=0):
        """To initialize the class, you need one variable
        Args:
            size (int): size of the square.
        """
        if (not (isinstance(size, int))):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
