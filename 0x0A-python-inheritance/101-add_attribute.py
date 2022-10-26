#!/usr/bin/python3
""" Module to define add_attribute
"""


def add_attribute(obj, attr, value):
    """ Function to add an attribute to an object if possible

    Args:
        obj (any): Object to add attribute to
        attr (str): Attribute to be added to obj
        value (any): Value of attr
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
