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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and Setter for width
    @property
    def width(self):
        """ Getter for Width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Getter and Setter for height
    @property
    def height(self):
        """ Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Getter and Setter for x
    @property
    def x(self):
        """ Getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Getter and Setter for y
    @property
    def y(self):
        """ Getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Return Area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """ Display rectangle using x and y
        """
        for i in range(self.y):
            print("")
        for h in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ Format output for Rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """ Update instance variables depending on input values
        """
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            for key in sorted(kwargs):
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ Return dictionary representation of rectangle
        """
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
