#!/usr/bin/python3
"""
This program takes two matrices and multiply them with the library numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Args: Takes two matrices and multiply them using the module NumPy
        :param m_a: list of lists (int or float)
        :param m_b: list of lists (int or float)
    """
    return np.matmul(m_a, m_b)
