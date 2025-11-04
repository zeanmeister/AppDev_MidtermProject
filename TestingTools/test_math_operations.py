# ======================================================
# test_math_operations.py
# Demonstrates testing and debugging in PyCharm
# ======================================================

import unittest
from math_operations import add, subtract, multiply, divide


class TestMathOperations(unittest.TestCase):

    # Demonstrates "Run Test" and "Rerun Failed Test"
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)

    # Demonstrates auto-generated test and parameter changes
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(5, 5), 25)

    # Demonstrates "Debug Test" and error inspection
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(9, 3), 3)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()
