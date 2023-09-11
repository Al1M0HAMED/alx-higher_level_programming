#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length > 0:
        biggest = my_list[0]
        for i in my_list:
            if i >= biggest:
                biggest = i
        return (int(biggest))
    else:
        return (None)
