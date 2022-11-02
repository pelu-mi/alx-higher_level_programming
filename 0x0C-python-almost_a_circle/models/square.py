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
