import Calculator
import unittest
import random


class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator.Calculator()

    def test_add_method(self):
        result = self.calculator.add(4, 2)
        self.assertEqual(6, result)

    def test_add_method_invalid_value(self):
        self.assertRaises(ValueError, self.calculator.add, "four", "five")

    def test_multiply_method(self):
        result = self.calculator.multiply(5, 3)
        self.assertEqual(15, result)

    def test_multiply_method_invalid_value(self):
        self.assertRaises(ValueError, self.calculator.multiply, "four", "five")

    def test_sub_method(self):
        result = self.calculator.sub(6, 4)
        self.assertEqual(2, result)

    def test_sub_method_invalid_value(self):
        self.assertRaises(ValueError, self.calculator.sub, "four", "five")

    def test_div_method(self):
        result = self.calculator.div(5, 1)
        self.assertEqual(5, result)

    def test_div_method_invalid_value(self):
        self.assertRaises(ValueError, self.calculator.div, "five", "four")

    def test_div_method_zero(self):
        self.assertRaises(ZeroDivisionError, self.calculator.div, 5, 0)


if __name__ == '__main__':
    unittest.main()
