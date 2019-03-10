#!/usr/bin/env python

__author__ = 'Aditya Verma'
__rollno__ = 2017009

import unittest
from ttt import game1
from ttt import game2
from ttt import game3
from ttt import validBoard
from ttt import validmove


class testpoint(unittest.TestCase):

    def test_game1(self):
        self.assertAlmostEqual(game1(10000), 0.5926, delta=0.1)

    def test_game2(self):
        self.assertEqual(game2(10000), 0)
        self.assertEqual(game2(1000), 0)
        self.assertEqual(game2(100), 0)
        self.assertEqual(game2(10), 0)
        self.assertEqual(game2(1), 0)

    def test_game3(self):
        self.assertEqual(game3(10000), 0)
        self.assertEqual(game3(1000), 0)
        self.assertEqual(game3(100), 0)
        self.assertEqual(game3(10), 0)
        self.assertEqual(game3(1), 0)

    def test_validBoard(self):
        self.assertTrue(validBoard())

    def test_validmove(self):
        self.assertFalse(validmove(1))
        self.assertFalse(validmove(2))
        self.assertFalse(validmove(3))
        self.assertFalse(validmove(4))
        self.assertFalse(validmove(5))


if __name__ == '__main__':
    unittest.main()
