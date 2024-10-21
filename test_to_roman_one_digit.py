import unittest

from Q2 import to_roman_one_digit


class TestToRoman(unittest.TestCase):
    def test_to_roman_one_digit_ones_one(self):
        actual = to_roman_one_digit(1)
        expected = "I"
        self.assertEqual(expected, actual)  # add assertion here

    def test_to_roman_one_digit_ones_three(self):
        actual = to_roman_one_digit(3)
        expected = "III"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_ones_four(self):
        actual = to_roman_one_digit(4)
        expected = "IV"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_ones_five(self):
        actual = to_roman_one_digit(5)
        expected = "V"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_ones_six(self):
        actual = to_roman_one_digit(6)
        expected = "VI"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_ones_eight(self):
        actual = to_roman_one_digit(8)
        expected = "VIII"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_ones_nine(self):
        actual = to_roman_one_digit(9)
        expected = "IX"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_tens_one(self):
        actual = to_roman_one_digit(10)
        expected = "X"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_tens_three(self):
        actual = to_roman_one_digit(30)
        expected = "XXX"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_tens_four(self):
        actual = to_roman_one_digit(40)
        expected = "XL"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_tens_five(self):
        actual = to_roman_one_digit(50)
        expected = "L"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_tens_six(self):
        actual = to_roman_one_digit(60)
        expected = "LX"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_tens_eight(self):
        actual = to_roman_one_digit(80)
        expected = "LXXX"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_tens_nine(self):
        actual = to_roman_one_digit(90)
        expected = "XC"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_hundreds_one(self):
        actual = to_roman_one_digit(100)
        expected = "C"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_hundreds_three(self):
        actual = to_roman_one_digit(300)
        expected = "CCC"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_hundreds_four(self):
        actual = to_roman_one_digit(400)
        expected = "CD"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_hundreds_five(self):
        actual = to_roman_one_digit(500)
        expected = "D"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_hundreds_six(self):
        actual = to_roman_one_digit(600)
        expected = "DC"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_hundreds_eight(self):
        actual = to_roman_one_digit(800)
        expected = "DCCC"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_hundreds_nine(self):
        actual = to_roman_one_digit(900)
        expected = "CM"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_thousands_one(self):
        actual = to_roman_one_digit(1000)
        expected = "M"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_thousands_three(self):
        actual = to_roman_one_digit(3000)
        expected = "MMM"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_thousands_four(self):
        actual = to_roman_one_digit(4000)
        expected = "MMMM"
        self.assertEqual(expected, actual)

    def test_to_roman_one_digit_thousands_five(self):
        actual = to_roman_one_digit(5000)
        expected = "MMMMM"
        self.assertEqual(expected, actual)
