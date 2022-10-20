#!/usr/bin/python3
""" Module for Matrix product
"""


def matrix_mul(m_a, m_b):
    """Function to multiply 2 matrices

    Args:
        m_a (list): List of list of numbers
        m_b (list): List of list of numbers

    Returns:
        List: Matrix product of m_a and m_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_a, list):
        raise TypeError("m_b must be a list")
    if len(m_a) != 0:
        for item in m_a:
            if not isinstance(item, list):
                raise TypeError("m_a must be a list of lists")
    if len(m_b) != 0:
        for item in m_b:
            if not isinstance(item, list):
                raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    a_len = len(m_a[0])
    for item in m_a:
        a = 0
        for i in range(0, len(item)):
            if not isinstance(item[i], int) and not isinstance(item[i], float):
                raise TypeError("m_a should contain only integers or floats")
            a = a + 1
        if a != a_len:
            raise TypeError("each row of m_a must be of the same size")
    b_len = len(m_b[0])
    for item in m_b:
        b = 0
        for i in range(0, len(item)):
            if not isinstance(item[i], int) and not isinstance(item[i], float):
                raise TypeError("m_b should contain only integers or floats")
            b = b + 1
        if b != b_len:
            raise TypeError("each row of m_b must be of the same size")
    # for matrix product to work, columns in m_a must be equal to rows in m_b
    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")
    # Now for the calculation
    result = []
    rows = len(m_a)  # New matrix rows = rows in m_a
    cols = len(m_b[0])  # New matrix columns = columns in m_b
    n = len(m_b)  # n represent number of rows in m_b or cols in m_a
    for r in range(0, rows):
        lis = []
        for c in range(0, cols):
            a = 0
            for i in range(0, n):
                a += m_a[r][i] * m_b[i][c]
            lis.append(a)
        result.append(lis)
    return result
