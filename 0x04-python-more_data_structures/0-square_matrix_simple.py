#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_raw = []
    for i in range(len(matrix)):
        if i:
            new_matrix.append(new_raw)
            new_raw = []
        for j in range(len(matrix[i])):
            new_raw.append(matrix[i][j] ** 2)
    new_matrix.append(new_raw)
    return (new_matrix)
