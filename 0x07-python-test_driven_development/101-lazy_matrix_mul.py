#!/usr/bin/python3
""" Module to compute matrix product using numpy
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function to find matrix product of two matrices

    Args:
        m_a (list): List of lists of integer or float
        m_b (list): List of lists of integer or float
    """
    return np.matmul(m_a, m_b)
