#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Main function
    Args:
    Raises:
    Return:
    """
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    new_matrix = [[None for _ in range(num_columns)] for _ in range(num_rows)]

    for i in range(num_rows):
        if num_columns != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(num_columns):
            if type(matrix[i][j]) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[i][j] = round((matrix[i][j] / div), 2)
    return new_matrix
