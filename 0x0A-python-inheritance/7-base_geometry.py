#!/usr/bin/python3
""" Module to define class BaseGeometry
"""


class BaseGeometry():
    """ Class BaseGeometry with methods area and integer_validator
    """

    def area(self):
        """ Function to raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validate value

        Args:
            name (str): Name
            value (int): Value to be validated
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
