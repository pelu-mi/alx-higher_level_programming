#!/usr/bin/python3
""" Module Documentation
"""


class Student:
    """ Student class with first_name, last_name and age as well as a
    public method, to_json
    """
    def __init__(self, first_name, last_name, age):
        """ Initialize Student with these 3 variables
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return dictionary representation of the object
        """
        if not isinstance(attrs, list):
            return self.__dict__
        for i in attrs:
            if not isinstance(i, str):
                return self.__dict__
        # Return a dict with only attributes in attrs
        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict

    def reload_from_json(self, json):
        """ Replaces all attribute values with the values in json dictionary
        """
        for item in json:
            setattr(self, item, json[item])
