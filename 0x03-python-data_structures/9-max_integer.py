#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = 0
    length = len(my_list)
    if length > 0:
        for i in my_list:
            if i >= biggest:
                biggest = i
        return (int(biggest))
    else:
        return (None)
