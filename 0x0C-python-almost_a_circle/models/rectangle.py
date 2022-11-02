#!/usr/bin/python3
""" Module for Rectangle class
"""


from .base import Base


class Rectangle(Base):
    """ Class Rectangle inherits from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize Rectangle with 7 variables
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # Getter and Setter for width
    @property
    def width(self):
        """ Getter for Width
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    # Getter and Setter for height
    @property
    def height(self):
        """ Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    # Getter and Setter for x
    @property
    def x(self):
        """ Getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    # Getter and Setter for y
    @property
    def y(self):
        """ Getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
