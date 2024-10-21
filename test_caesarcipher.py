import unittest

from Q3 import caesarcipher


class MyTestCase(unittest.TestCase):
    def test_caesarcipher_empty_message(self):
        actual = caesarcipher("", True, 1)
        expected = ""
        self.assertEqual(expected, actual)  # add assertion here

    def test_caesarcipher_encode_numbers(self):
        actual = caesarcipher("123", True, 1)
        expected = "123"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encode_symbols(self):
        actual = caesarcipher("()", True, 1)
        expected = "()"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encode_mixed(self):
        actual = caesarcipher("Abc123:/", True, 1)
        expected = "Bcd123:/"
        self.assertEqual(expected, actual)

    def test_caesarcipher_decode_numbers(self):
        actual = caesarcipher("123", False, 1)
        expected = "123"
        self.assertEqual(expected, actual)

    def test_caesarcipher_decode_symbols(self):
        actual = caesarcipher("()", False, 1)
        expected = "()"
        self.assertEqual(expected, actual)

    def test_caesarcipher_decode_mixed(self):
        actual = caesarcipher("Abc123:/", False, 1)
        expected = "Zab123:/"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encode_long_message(self):
        actual = caesarcipher("I love my pet bird, Tofu. :)", True, 10)
        expected = "S vyfo wi zod lsbn, Dype. :)"
        self.assertEqual(expected, actual)

    def test_caesarcipher_decode_long_message(self):
        actual = caesarcipher("S vyfo wi zod lsbn, Dype. :)", False, 10)
        expected = "I love my pet bird, Tofu. :)"
        self.assertEqual(expected, actual)

    def test_caesarcipher_all_lowercase(self):
        actual = caesarcipher("cat", True, 1)
        expected = "dbu"
        self.assertEqual(expected, actual)

    def test_caesarcipher_all_uppercase(self):
        actual = caesarcipher("CAT", True, 1)
        expected = "DBU"
        self.assertEqual(expected, actual)

    def test_caesarcipher_positive_encode_within_period(self):
        actual = caesarcipher("Abc", True, 25)
        expected = "Zab"
        self.assertEqual(expected, actual)

    def test_caesarcipher_positive_encode_on_period(self):
        actual = caesarcipher("aBc", True, 26)
        expected = "aBc"
        self.assertEqual(expected, actual)

    def test_caesarcipher_positive_encode_beyond_period(self):
        actual = caesarcipher("xyZ", True, (26*3) + 1)
        expected = "yzA"
        self.assertEqual(expected, actual)

    def test_caesarcipher_negative_encode_within_period(self):
        actual = caesarcipher("Zab", True, -25)
        expected = "Abc"
        self.assertEqual(expected, actual)

    def test_caesarcipher_negative_encode_on_period(self):
        actual = caesarcipher("aBc", True, -26)
        expected = "aBc"
        self.assertEqual(expected, actual)

    def test_caesarcipher_negative_encode_beyond_period(self):
        actual = caesarcipher("yzA", True, -((26*3) + 1))
        expected = "xyZ"
        self.assertEqual(expected, actual)

    def test_caesarcipher_positive_decode_within_period(self):
        actual = caesarcipher("Zab", False, 25)
        expected = "Abc"
        self.assertEqual(expected, actual)

    def test_caesarcipher_positive_decode_on_period(self):
        actual = caesarcipher("aBc", False, 26)
        expected = "aBc"
        self.assertEqual(expected, actual)

    def test_caesarcipher_positive_decode_beyond_period(self):
        actual = caesarcipher("yzA", False, (26*3) + 1)
        expected = "xyZ"
        self.assertEqual(expected, actual)

    def test_caesarcipher_negative_decode_within_period(self):
        actual = caesarcipher("Abc", False, -25)
        expected = "Zab"
        self.assertEqual(expected, actual)

    def test_caesarcipher_negative_decode_on_period(self):
        actual = caesarcipher("aBc", False, -26)
        expected = "aBc"
        self.assertEqual(expected, actual)

    def test_caesarcipher_negative_decode_beyond_period(self):
        actual = caesarcipher("xyZ", False, -((26*3) + 1))
        expected = "yzA"
        self.assertEqual(expected, actual)
