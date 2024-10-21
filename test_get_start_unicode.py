from unittest import TestCase

from Q3 import get_start_unicode


class TestGetStartUnicode(TestCase):
    def test_get_start_unicode_lowercase(self):
        actual = get_start_unicode('b')
        expected = ord('a')
        self.assertEqual(expected, actual)

    def test_get_start_unicode_uppercase(self):
        actual = get_start_unicode('B')
        expected = ord('A')
        self.assertEqual(expected, actual)

    def test_get_start_unicode_non_alphanumeric(self):
        actual = get_start_unicode('/')
        expected = ord('/')
        self.assertEqual(expected, actual)

    def test_get_start_unicode_number(self):
        actual = get_start_unicode('1')
        expected = ord('1')
        self.assertEqual(expected, actual)