#!/usr/bin/python3
""" Module Documentation
"""


def text_indentation(text):
    """ Function to print out a text with indentation

    Args:
        text (str): Text to be printed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for c in text:
        if c == '.' or c == '?' or c == ':':
            print("{}\n".format(c))
            flag = 1
            continue
        if flag == 1 and c == " ":
            continue
        elif flag == 1 and c != " ":
            flag = 0
        print("{}".format(c), end="")
