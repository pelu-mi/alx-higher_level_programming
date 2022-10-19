#!/usr/bin/python3
"""Define a function to add 2 integers

Only one Function is defined here

"""


def add_integer(a, b=98):
    """Function to Add 2 numbers together
    Raises:
        TypeError: if either of the 2 values is not an int or float"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
