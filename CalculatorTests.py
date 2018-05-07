import Calculator
import unittest


class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.c = Calculator.Calculator()

    def test_add_method(self):
        result = self.c.add(4, 2)
        self.assertEqual(6, result)

    def test_add_method_invalid_value(self):
        self.assertRaises(ValueError, self.c.add, "four", "five")

    def test_multiply_method(self):
        result = self.c.multiply(5, 3)
        self.assertEqual(15, result)

    def test_multiply_method_invalid_value(self):
        self.assertRaises(ValueError, self.c.multiply, "four", "five")

    def test_sub_method(self):
        result = self.c.sub(6, 4)
        self.assertEqual(2, result)

    def test_sub_method_invalid_value(self):
        self.assertRaises(ValueError, self.c.sub, "four", "five")

    def test_div_method(self):
        result = self.c.div(5, 1)
        self.assertEqual(5, result)

    def test_div_method_invalid_value(self):
        self.assertRaises(ValueError, self.c.div, "five", "four")

    def test_div_method_zero(self):
        self.assertRaises(ZeroDivisionError, self.c.div, 5, 0)


if __name__ == '__main__':
    unittest.main()
