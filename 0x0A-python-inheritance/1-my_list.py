#!/usr/bin/python3
"""
date: 15 / 11 / 2025
auther: Ali Mohamed
"""


class MyList(list):
    """" basic list operations """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
