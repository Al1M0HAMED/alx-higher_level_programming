#!/usr/bin/python3
# this function checks if c is lower case if return True else False

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
