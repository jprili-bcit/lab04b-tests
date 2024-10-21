import unittest

from Q2 import get_roman_unit


class TestGetRomanUnit(unittest.TestCase):
    def test_get_roman_unit_ones(self):
        actual = get_roman_unit(0)
        expected = 'I'
        self.assertEqual(expected, actual)  # add assertion here

    def test_get_roman_unit_tens(self):
        actual = get_roman_unit(1)
        expected = 'X'
        self.assertEqual(expected, actual)

    def test_get_roman_unit_hundreds(self):
        actual = get_roman_unit(2)
        expected = 'C'
        self.assertEqual(expected, actual)

    def test_get_roman_unit_thousands(self):
        actual = get_roman_unit(3)
        expected = 'M'
        self.assertEqual(expected, actual)
