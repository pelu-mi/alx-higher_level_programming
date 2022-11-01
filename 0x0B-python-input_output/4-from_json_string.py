#!/usr/bin/python3
""" Module documentation
"""


import json


def from_json_string(my_str):
    """ Function to convert json string to object

    Args:
        my_str (str): JSON string

    Returns:
        any: Object represented by JSON string
    """
    return json.loads(my_str)
