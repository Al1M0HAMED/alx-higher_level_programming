#!/usr/bin/python3
import sys
from locale import atoi
if __name__ == '__main__':
    av = sys.argv
    ac = len(av)
    sum = 0
    if ac > 1:
        for i in range(1, ac):
            sum += atoi(av[i])
    print("{:d}".format(sum))
