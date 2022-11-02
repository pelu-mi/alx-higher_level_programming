#!/usr/bin/python3
""" Module to define class Square
"""


from .rectangle import Rectangle


class Square(Rectangle):
    """ Class Square inheriting from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Format printing of Square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    # Getter and Setter for size
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
