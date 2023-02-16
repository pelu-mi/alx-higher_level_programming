#!/usr/bin/python3
""" Module for interview prep
"""

def find_peak(list_of_integers):
    """ Function to find peak in a list of integers
    """
    list_of_integers.sort()
    if (list_of_integers == []):
        return None
    else:
        return (list_of_integers[-1])
