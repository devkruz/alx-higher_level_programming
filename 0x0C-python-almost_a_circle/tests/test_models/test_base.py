#!/usr/bin/python3
"""
unittest Base class:
    Test_init - line

"""
import unittest
from models.base import Base


class Test_init(unittest.TestCase):
    """ Test base class init method """
    def test_no_arg(self):
        """ Initialize without arguments """
        b1 = Base()
        b2 = Base()
        self.assertAlmostEqual(b2.id, (b1.id + 1))

    def test_arg(self):
        """ Initialize with argument """
        b1 = Base(44)
        b2 = Base(41)
        self.assertAlmostEqual(b1.id, 44)
        self.assertEqual(b2.id, 41)
