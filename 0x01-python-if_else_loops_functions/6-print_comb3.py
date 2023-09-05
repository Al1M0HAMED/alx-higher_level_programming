#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j != i and (j - i)> 0:
            if i != 8:
                print("{:02d}".format(i * 10 + j), end=", ")
            else:
                print("{:02d}".format(i * 10 + j))
