#!/usr/bin/python3
"""a function that prints x elements of a list.
    All elements must be printed on the same line followed by a new line
    x represents the number of elements to print
    x can be bigger than the length of my_list
    Return the real number of elements printed
    """


def safe_print_list(my_list=[], x=0):
    i = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            i += 1
        except IndexError:
            break
    print("")
    return (i)
