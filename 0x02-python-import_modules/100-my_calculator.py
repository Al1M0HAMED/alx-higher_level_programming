#!/usr/bin/python3
import sys
from locale import atoi
from calculator_1 import sub, mul, add, div
if __name__ == '__main__':
    av = sys.av
    ac = len(av)
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if av[2] != '+' or '-' or '*' or '/':

