#!/usr/bin/python3
""" Module for Base class
"""


import json


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

    def to_json_string(list_dictionaries):
        """ Class Method to convert input to json string

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            str: JSON representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        json_string = ""
        for dictionary in list_dictionaries:
            json_string += json.dumps(dictionary)
        return json_string
