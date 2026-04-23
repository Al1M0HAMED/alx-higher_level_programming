#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_pass(self):
        self.assertEqual(max_integer([0, 5, 3, 2, 2]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([0, 1, 2, 5]), 5)
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_fail(self):
        self.assertRaises(TypeError, max_integer, 1.5)
        self.assertRaises(TypeError, max_integer, 1)
