#!/usr/bin/python3
""" Module defining MyInt inheriting from int
"""


class MyInt(int):
    """ Class MyInt inheriting from int with == and != operations inverted
    """

    def __eq__(self, other):
        """ Inverted equal to operation
        """
        return int(self) != int(other)

    def __ne__(self, other):
        """ Inverted not equal to operation
        """
        return int(self) == int(other)
