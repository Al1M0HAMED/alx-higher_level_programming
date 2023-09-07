#!/usr/bin/python3
import sys
if __name__ == '__main__':
    arguments = sys.argv
    argc = len(arguments)
    print("{} arguments.".format(argc - 1))
    if argc > 1:
        for i in range(1, argc):
            print("{}: {}".format(i, arguments[i]))
