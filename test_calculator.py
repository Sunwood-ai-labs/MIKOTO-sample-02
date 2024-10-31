import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_add(self):
        """加算のテスト"""
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)









    def test_subtract(self):
        """減算のテスト"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)




    def test_multiply(self):
        """乗算のテスト"""
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)



    def test_divide(self):
        """除算のテスト"""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_divide_by_zero(self):
        """0での除算のテスト"""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)


if __name__ == "__main__":
    unittest.main()
