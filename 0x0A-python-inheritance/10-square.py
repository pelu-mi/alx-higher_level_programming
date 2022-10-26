#!/usr/bin/python3
""" Module to define class Square inheriting from class Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square inheriting from class Rectangle
    """

    def __init__(self, size):
        """ Initialize Square as Rectangle with same size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
