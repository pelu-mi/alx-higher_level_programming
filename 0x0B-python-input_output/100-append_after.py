#!/usr/bin/python3
""" Module to insert line of text in a file after a line contains a specific
string
"""


def append_after(filename="", search_string="", new_string=""):
    """ Function to insert line of text in a file after a line that contains
    a specific string

    Args:
        filename (str): Name of file
        search_string (str): String to be searched for
        new_string (str): String to be inserted after line with search string
    """
    # Open file with append + mode
    with open(filename, 'r+', encoding='utf-8') as f:
        lines = []
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
        f.seek(0)
        f.write("".join(lines))
