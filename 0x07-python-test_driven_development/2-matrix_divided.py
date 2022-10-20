#!/usr/bin/python3
"""Module documentation
"""


def matrix_divided(matrix, div):
    """Function to divide a matrix by a single number

    Args:
        matrix(:obj: 'list' of :obj: 'list'): matrix of ints or floats
        div(int or float): Divisor

    Returns:
        List: Matrix with each element divided by divisor
    """
    if not isinstance(matrix, list):# check if matrix is a list
        raise TypeError("matrix must be a matrix (list of lists) of
                integers/floats")
    for row in range(0, len(matrix)):
        if not isinstance(matrix[row], list):# check if each element is a list
            raise TypeError("matrix must be a matrix (list of lists) of
                    integers/floats")
        r = 0
        for col in matrix[row]:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError("matrix must be a matrix (list of lists) of
                        integers/floats")# check if items is int or float
            r = r + 1
        if r != row_matrix:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_matrix = len(matrix[0])# length of the first row in the matrix
    result = []
    for i in range(0, len(matrix)):
        new_row = []
        for col in matrix[i]:
            new_row.append(round(col/div, 2))
        result.append(new_row)# Find a simpler way to do this
    return result
