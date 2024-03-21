#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""

    for x in matrix:
        print(" ".join("{:d}".format(y) for y in x))
