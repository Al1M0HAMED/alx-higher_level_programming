#!/usr/bin/python3
"""
date: 8 / 11 / 2025
auther: Ali Mohamed
"""


class MyList(list):
    """" basic list operations """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
