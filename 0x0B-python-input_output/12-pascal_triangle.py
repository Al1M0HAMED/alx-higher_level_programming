#!/usr/bin/python3
"""
pascal p
"""

"""
returns a list of lists of integers representing the Pascal’s triangle of n
"""
def pascal_triangle(n):
    pascal_list = []
    i = 0
    while i < n:
        inner_list = []
        j = 0
        while j <= i:
            if j == i or i == 0 or i == 1 or j == 0:
                inner_list.append(1)
            else:
                inner_list.append(pascal_list[i - 1][j]
                                  + pascal_list[i - 1][j - 1])
            j += 1
        pascal_list.append(inner_list)
        i += 1
    return (pascal_list)
