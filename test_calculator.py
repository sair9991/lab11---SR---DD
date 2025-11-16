# https://github.com/sair9991/lab11---SR---DD.git

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 5), -5)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(6, 2), 3)
        self.assertEqual(div(-9, 3), -3)
        self.assertEqual(div(10, 2), 5)

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
    def test_add(self):
        self.assertEqual(add(5, 8), 13)
        self.assertEqual(add(-2, -7), -9)
        self.assertEqual(add(0,0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(12, 5),7)
        self.assertEqual(subtract(-10, -2), -8)
        self.assertEqual(subtract(0, 5), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)


    def test_logarithm(self): # 3 assertions
         self.assertEqual(logarithm(2, 8), 3)
         self.assertEqual(logarithm(3, 27), 3)
         self.assertEqual(logarithm(2, 16), 4)

    def test_log_invalid_base(self):
         with self.assertRaises(ValueError):
            logarithm(0, 3)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
