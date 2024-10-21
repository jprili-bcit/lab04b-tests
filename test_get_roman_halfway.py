import unittest

from Q2 import get_roman_halfway


class TestGetRomanHalfway(unittest.TestCase):
    def test_get_roman_halfway_ones(self):
        actual = get_roman_halfway(0)
        expected = 'V'
        self.assertEqual(expected, actual)  # add assertion here

    def test_get_roman_halfway_tens(self):
        actual = get_roman_halfway(1)
        expected = 'L'
        self.assertEqual(expected, actual)

    def test_get_roman_halfway_hundreds(self):
        actual = get_roman_halfway(2)
        expected = 'D'
        self.assertEqual(expected, actual)

    def test_get_roman_halfway_thousands(self):
        actual = get_roman_halfway(3)
        expected = ''
        self.assertEqual(expected, actual)
