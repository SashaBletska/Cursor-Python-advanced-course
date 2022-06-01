import unittest
from functions_to_test import *


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(1, 2), 3)
        self.assertEqual(Calculator.add(20, -10), 10)
        self.assertNotEqual(Calculator.add(5, 20), 52)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(24, 9), 15)
        self.assertEqual(Calculator.subtract(100, 105), -5)
        self.assertNotEqual(Calculator.subtract(1000, 5), 95)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 4), 8)
        self.assertEqual(Calculator.multiply(50, 0.2), 10)
        self.assertNotEqual(Calculator.multiply(10, 10), 1000)

    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 2), 5)
        self.assertEqual(Calculator.divide(10, 20), 0.5)
        self.assertNotEqual(Calculator.divide(10, 1), 1)
        self.assertRaises(ValueError, Calculator.divide, 100, 0)

