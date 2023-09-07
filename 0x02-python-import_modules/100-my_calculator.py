#!/usr/bin/python3
import sys
from locale import atoi
from calculator_1 import sub, mul, add, div
if __name__ == '__main__':
    av = sys.argv
    ac = len(av)
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = av[2]
    a, b = atoi(av[1]), atoi(av[3])
    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif op == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    sys.exit()
