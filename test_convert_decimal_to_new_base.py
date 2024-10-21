import unittest

from Q1 import convert_decimal_to_new_base


class TestConvertDecimalToNewBase(unittest.TestCase):
    def test_convert_decimal_to_new_base_zero_min_base(self):
        actual = convert_decimal_to_new_base(2, 0)
        expected = '0'
        self.assertEqual(expected, actual)  # add assertion here

    def test_convert_decimal_to_new_base_zero_max_base(self):
        actual = convert_decimal_to_new_base(9, 0)
        expected = '0'
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_new_base_non_zero_min_base(self):
        actual = convert_decimal_to_new_base(2, 1)
        expected = '1'
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_new_base_non_zero_max_base(self):
        actual = convert_decimal_to_new_base(9, 1)
        expected = '1'
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_new_base_two_places_min_base(self):
        actual = convert_decimal_to_new_base(2, 3)
        expected = '11'
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_new_base_two_places_max_base(self):
        actual = convert_decimal_to_new_base(9, 10)
        expected = '11'
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_new_base_num_equal_base_min_base(self):
        actual = convert_decimal_to_new_base(2, 2)
        expected = '10'
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_new_base_num_equal_base_max_base(self):
        actual = convert_decimal_to_new_base(9, 9)
        expected = '10'
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_new_base_non_zero_other_base(self):
        actual = convert_decimal_to_new_base(4, 6)
        expected = '12'
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_new_base_bigger_number(self):
        actual = convert_decimal_to_new_base(2, 33)
        expected = '100001'
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_new_base_before_new_place(self):
        actual = convert_decimal_to_new_base(9, 531440)
        expected = '888888'
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_new_base_after_new_place(self):
        actual = convert_decimal_to_new_base(9, 531441)
        expected = '1000000'
        self.assertEqual(expected, actual)
