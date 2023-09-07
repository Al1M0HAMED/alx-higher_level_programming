#!/usr/bin/python3
import sys
if __name__ == '__main__':
    arguments = sys.argv
    ac = len(arguments)
    print("{} argument{}{}".format(ac - 1, "s" if ac != 2 else "", ":" if ac > 1 else "."))
    if ac > 1:
        for i in range(1, ac):
            print("{}: {}".format(i, arguments[i]))
