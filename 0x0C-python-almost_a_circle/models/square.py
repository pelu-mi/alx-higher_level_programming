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

    def update(self, *args, **kwargs):
        """ Update instance variables depending on input values
        """
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            for key in sorted(kwargs):
                setattr(self, key, kwargs[key])
