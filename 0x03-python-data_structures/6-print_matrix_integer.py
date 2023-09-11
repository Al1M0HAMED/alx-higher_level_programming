#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in range(len(matrix)):
        for i in range(len(matrix[l])):
            print("{}{}".format(" " if i != 0 else "", matrix[l][i]), end="")
        print("")
