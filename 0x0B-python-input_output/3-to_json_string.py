#!/usr/bin/python3
""" Module Documentation
"""


import json


def to_json_string(my_obj):
    """ Function to convert an object to JSON string

    Args:
        my_obj (any): Object to be representon in JSON

    Returns:
        str: JSON representation of my_obj
    """
    return json.dumps(my_obj)
