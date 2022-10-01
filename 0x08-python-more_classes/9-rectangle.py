#!/usr/bin/python3
"""This Module is for class Rectangle"""


class Rectangle:
    """This is a class Rectangle

    Attributes:
        number_of_instances (int): number of instances
        print_symbol (:obj:'str'): print symbol
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize Rectangle

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def height(self):
        """int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """int: Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """Area of rectangle

        Returns:
            int: height * width
        """
        return self.__height * self.__width

    def perimeter(self):
        """Perimeter of rectangle

        Returns:
            int: 2(height + width) or 0
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Format print of Rectangle object
        """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        height = self.__height
        width = self.__width
        for i in range(0, height):
            for j in range(0, width):
                string += str(self.print_symbol)
            if i != height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """Format print (repr) of Rectangle object
        """
        width = str(self.__width)
        height = str(self.__height)
        return "Rectangle(" + width + ", " + height + ")"

    def __del__(self):
        """Action to take after deleting Rectangle object
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Check which rectangle is bigger based on Area

        Args:
            rect_1 (:obj:'Rectangle'): Rectangle to be checked
            rect_2 (:obj:'Rectangle'): Rectangle to be checked
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Create a new instance of Rectangle with width=height=size

        Args:
            size (int): Size of new Rectangle
        """
        return Rectangle(size, size)
