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

    def area(self):
        """ Calculate and return area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """ Format output to '[Rectangle] <width>/<height>'
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
