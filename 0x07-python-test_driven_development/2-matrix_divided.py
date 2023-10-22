#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Main function
    Args:
    Raises:
    Return:
    """
    new = [[0, 0, 0], [0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new[i][j] = round((matrix[i][j] / div), 2)
    return new
