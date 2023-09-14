#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0] if rows > 0 else 0)
    new_list = [[None] * cols for x in range(rows)]
    for row in range(rows):
        for col in range(cols):
            new_list[row][col] = matrix[row][col] ** 2
    return new_list
