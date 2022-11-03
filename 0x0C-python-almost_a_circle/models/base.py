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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Class Method to convert input to json string

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            str: JSON representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method to write json representation of list_objs to a file
        with a filename <class name>.json

        Args:
            list_objs (list): List of instances inheriting from Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dict))
