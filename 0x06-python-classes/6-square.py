#!/usr/bin/python3
"""This Module is for a class Square"""


class Square:
    """This is a class that defines Square with a size"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the class Square

        Args:
            size (int): size of the square.
            position (:obj:'tuple' of :obj:'int'): position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """This is the position of the Square"""
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not (isinstance(value[0], int)) or not (isinstance(value[1], int)):
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print out the square"""
        if self.__size == 0:
            print("")
            return
        size = self.__size
        position = self.__position
        if position[1] != 0:
            for c in range(0, position[1]):
                print("")
        for i in range(1, size + 1):
            if position[0] != 0:
                for k in range(0, position[0]):
                    print(" ", end="")
            for j in range(0, size):
                print("#", end="")
            print("")
