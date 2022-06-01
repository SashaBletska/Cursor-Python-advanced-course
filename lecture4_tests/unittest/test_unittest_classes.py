import unittest
from class_to_test import *


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(10, 2)

    def test_add(self):
        self.assertEqual(self.calculator.add(), 12)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(), 8)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(), 20)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(), 5)
