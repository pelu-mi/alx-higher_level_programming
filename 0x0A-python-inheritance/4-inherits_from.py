#!/usr/bin/python3
""" Module for inherits_from function
"""


def inherits_from(obj, a_class):
    """ Function to check if obj is an instance of a subclass of a_class

    Args:
        obj (:obj:): An instance of an object
        a_class (:cls:): A class or datatype

    Returns:
        bool: True if obj is an instance of a subclass of a_class
        else, False
    """
    return issubclass(type(obj), a_class) and not (type(obj) is a_class)
