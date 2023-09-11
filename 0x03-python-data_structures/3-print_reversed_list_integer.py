#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    for i in range(length, -1, -1):
        if i > 0:
            print("{}".format(my_list[i - 1]))
