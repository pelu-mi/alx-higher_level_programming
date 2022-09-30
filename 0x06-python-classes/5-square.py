#!/usr/bin/python3
"""This Module is for a class Square"""


class Square:
    """This is a class that defines Square with a size"""

    def __init__(self, size=0):
        """Initialize the class Square

        Args:
            size (int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """This is the size of the Square"""
        return self.__size

    @size.setter
    def size(self, value):
        if (not (isinstance(value, int))):
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print out the square"""
        if self.__size == 0:
            print("")
            return
        size = self.__size
        for i in range(1, size + 1):
            for j in range(0, size):
                print("#", end="")
            print("")
