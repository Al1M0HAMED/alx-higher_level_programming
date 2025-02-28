#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_pass(self):
        """ tests that are expected to passs """
        self.assertEqual(max_integer([0, 5, 3, 2, 2]), 5)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_fail(self):
        """ tests that are expected to fail with Error """
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, 1.5)
