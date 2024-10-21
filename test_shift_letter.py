from unittest import TestCase

from Q3 import shift_letter


class TestShiftLetter(TestCase):
    def test_shift_letter_uppercase_within_period(self):
        actual = shift_letter("A", 25)
        expected = "Z"
        self.assertEqual(expected, actual)

    def test_shift_letter_uppercase_one_period(self):
        actual = shift_letter("A", 26)
        expected = "A"
        self.assertEqual(expected, actual)

    def test_shift_letter_uppercase_beyond_period(self):
        actual = shift_letter("A", 27)
        expected = "B"
        self.assertEqual(expected, actual)

    def test_shift_letter_lowercase_within_period(self):
        actual = shift_letter("a", 25)
        expected = "z"
        self.assertEqual(expected, actual)

    def test_shift_letter_lowercase_one_period(self):
        actual = shift_letter("a", 26)
        expected = "a"
        self.assertEqual(expected, actual)

    def test_shift_letter_lowercase_beyond_period(self):
        actual = shift_letter("a", 27)
        expected = "b"
        self.assertEqual(expected, actual)

    def test_shift_letter_non_alphabet_within_period(self):
        actual = shift_letter("/", 25)
        expected = "/"
        self.assertEqual(expected, actual)

    def test_shift_letter_non_alphabet_one_period(self):
        actual = shift_letter("/", 26)
        expected = "/"
        self.assertEqual(expected, actual)

    def test_shift_letter_non_alphabet_beyond_period(self):
        actual = shift_letter("/", 27)
        expected = "/"
        self.assertEqual(expected, actual)

    # no shifts
    def test_shift_letter_uppercase_no_shift(self):
        actual = shift_letter("A", 0)
        expected = "A"
        self.assertEqual(expected, actual)

    def test_shift_letter_lowercase_no_shift(self):
        actual = shift_letter("a", 0)
        expected = "a"
        self.assertEqual(expected, actual)

    def test_shift_letter_non_alphabet_no_shift(self):
        actual = shift_letter("/", 0)
        expected = "/"
        self.assertEqual(expected, actual)
