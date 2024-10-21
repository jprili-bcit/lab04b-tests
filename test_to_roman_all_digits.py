import unittest

from Q2 import to_roman_all_digits


class TestToRomanAllDigits(unittest.TestCase):
    def test_to_roman_all_digits_min(self):
        actual = to_roman_all_digits(1)
        expected = "I"
        self.assertEqual(expected, actual)  # add assertion here

    def test_to_roman_all_digits_max(self):
        actual = to_roman_all_digits(5000)
        expected = "MMMMM"
        self.assertEqual(expected, actual)

    def test_to_roman_all_digits_ones_four(self):
        actual = to_roman_all_digits(4)
        expected = "IV"
        self.assertEqual(expected, actual)

    def test_to_roman_all_digits_ones_five(self):
        actual = to_roman_all_digits(5)
        expected = "V"
        self.assertEqual(expected, actual)

    def test_to_roman_all_digits_ones_six(self):
        actual = to_roman_all_digits(6)
        expected = "VI"
        self.assertEqual(expected, actual)

    def test_to_roman_all_digits_ones_eight(self):
        actual = to_roman_all_digits(8)
        expected = "VIII"
        self.assertEqual(expected, actual)

    def test_to_roman_all_digits_ones_nine(self):
        actual = to_roman_all_digits(9)
        expected = "IX"
        self.assertEqual(expected, actual)

    def test_to_roman_all_digits_tens_mixed(self):
        actual = to_roman_all_digits(28)
        expected = "XXVIII"
        self.assertEqual(expected, actual)

    def test_to_roman_all_digits_hundreds_mixed(self):
        actual = to_roman_all_digits(168)
        expected = "CLXVIII"
        self.assertEqual(expected, actual)

    def test_to_roman_all_digits_thousands_mixed(self):
        actual = to_roman_all_digits(4321)
        expected = "MMMMCCCXXI"
        self.assertEqual(expected, actual)
