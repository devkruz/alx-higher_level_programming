#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer([..])"""

    def test_empty_list(self):
        """Test empty list"""
        self.assertAlmostEqual(max_integer([]), None)

    def test_ordered_list(self):
        """Test ordered list"""
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list"""
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_value_at_begining(self):
        """Test max value at the begining"""
        self.assertAlmostEqual(max_integer([4, 1, 3, 2]), 4)

    def test_list_of_float(self):
        """Test list of float"""
        self.assertAlmostEqual(max_integer([1.5, 3.7, 4.32, 2.21]), 4.32)

    def test_empty_string(self):
        """Test empty string"""
        self.assertAlmostEqual(max_integer(""), None)

    def test_string(self):
        """Test string"""
        self.assertAlmostEqual(max_integer("Adetola"), "t")

    def test_list_string(self):
        """Test list of string"""
        self.assertAlmostEqual(max_integer(["One", "Two", "Three"]), "Two")
