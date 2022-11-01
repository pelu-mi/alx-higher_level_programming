#!/usr/bin/python3
""" Module Documentation
"""


import json


def load_from_json_file(filename):
    """ Function to create object from json file

    Args:
        filename (str): Name of file containing Json representation

    Returns:
        any: Object represented by json file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
