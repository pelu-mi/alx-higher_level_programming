#!/usr/bin/python3
""" Module for Base class
"""


class Base:
    """ Class Base
    This class represents the base class of the project.
    It has a class attribute __nb_objects serves as the number of
    class objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize Base class with id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects