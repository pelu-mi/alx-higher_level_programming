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
        """This function returns the area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """This function performs == operation"""
        return self.area() == other.area()

    def __ne__(self, other):
        """This function performs != operation"""
        return self.area() != other.area()

    def __gt__(self, other):
        """This function performs > operation"""
        return self.area() > other.area()

    def __ge__(self, other):
        """This function performs >= operation"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """This function performs < operation"""
        return self.area() < other.area()

    def __le__(self, other):
        """This function performs <= operation"""
        return self.area() <= other.area()
