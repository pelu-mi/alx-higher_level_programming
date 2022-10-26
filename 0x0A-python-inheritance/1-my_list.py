#!/usr/bin/python3
""" Module to define MyList class
"""


class MyList(list):
    """ Class MyList with parent class list
    """

    def print_sorted(self):
        """ Method to print sorted list of members
        """
        copy = self[:]
        copy.sort()
        print(copy)
