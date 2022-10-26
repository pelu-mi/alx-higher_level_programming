#!/usr/bin/python3
""" Module defining Rectangle inheriting from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle inheriting from BaseGeometry
    """

    def __init__(self, width, height):
        """ Initialize rectangle with width and height
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
