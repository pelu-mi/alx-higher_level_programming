#!/usr/bin/python3
"""Module Documentation
"""


def print_square(size):
    """Function to print a square with dimensions of size

    Args:
        size (int): size of square to be printed
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size)
