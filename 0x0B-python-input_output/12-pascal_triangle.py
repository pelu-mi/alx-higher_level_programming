#!/usr/bin/python3
""" Module for Technical interview - Pascal triangle
"""


def pascal_triangle(n):
    """ Function to return a list of list of integers
    representing pascal triangle

    Args:
        n (int): Number of rows in pascal triangle

    Returns:
        list: List of list of integers
    """
    # loop n times
    if n <= 0:
        return []
    pascal = []
    row = 0
    prev = []
    while True:
        # Break if number of rows is complete
        if len(pascal) >= n:
            break
        # Handle first row
        if row == 0:
            pascal.append([1])
            row = row + 1
            continue
        # Handle second row and below
        lis = [1]
        prev = pascal[row - 1]
        for i in range(1, row):
            lis.append((prev[i - 1] + prev[i]))
        lis.append(1)
        pascal.append(lis)
        row = row + 1
    # Return pascal triangle
    return pascal
