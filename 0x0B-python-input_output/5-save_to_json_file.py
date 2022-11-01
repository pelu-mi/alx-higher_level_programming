#!/usr/bin/python3
""" Module documentation
"""


import json


def save_to_json_file(my_obj, filename):
    """ Function to save json representation of object to file

    Args:
        my_obj (any): Object to convert to Json representation
        filename (str): name of file to save json representation
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
