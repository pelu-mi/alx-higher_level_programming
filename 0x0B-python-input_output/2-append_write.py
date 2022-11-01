#!/usr/bin/python3
""" Module Documentation
"""


def append_write(filename="", text=""):
    """ Function to write text to a file with UTF8 encoding and
    return the number of chars written

    Args:
        filename (str): Name of file to write to
        text (str): String to write into file

    Returns:
        Total number of characters written
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
