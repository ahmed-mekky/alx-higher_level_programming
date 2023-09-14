#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_arr = []
    for row in matrix:
        new_arr[row] = []
        for col in row:
            new_arr[col] = matrix[col] ** 2
    return new_arr
