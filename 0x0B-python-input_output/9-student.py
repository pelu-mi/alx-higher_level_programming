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

    def to_json(self):
        """ Return dictionary representation of the object
        """
        return self.__dict__
