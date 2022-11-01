#!/usr/bin/python3
""" Module Documentation
"""


def read_file(filename=""):
    """ Function to read a text file (UTF8) and print it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
