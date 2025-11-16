import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(6, 2) 3)
        self.assertEqual(divide(-9, 3), -3)
        self.assertEqual(divide(10, 2) 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)
           
    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse(5, 12), 13.0)
        self.assertEqual(hypotenuse(8, 15), 17.0)

    def test_sqrt(self):
        self.assertEqual(square_root(16), 4.0)
        self.assertEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()