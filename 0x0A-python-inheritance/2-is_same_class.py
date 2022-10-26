#!/usr/bin/python3
""" Module for is_same_class function
"""


def is_same_class(obj, a_class):
    """ Function to check if obj is an instance of a_class

    Args:
        obj (:obj:): An instance of an object
        a_class (:cls:): A class or datatype

    Returns:
        bool: True if obj is an instance of a_class else, False
    """
    return (type(obj) is a_class)
