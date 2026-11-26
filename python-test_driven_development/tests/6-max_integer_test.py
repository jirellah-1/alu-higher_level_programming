#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines the unittests of the function max_integer."""

    def test_ordered_list(self):
        """Test a list in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list where the max is not at the ends."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list in descending order."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_second_position(self):
        """Test a list where the max is the second element."""
        self.assertEqual(max_integer([1, 5, 2]), 5)

    def test_two_elements(self):
        """Test lists of two elements in both orders."""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)

    def test_one_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test that an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Test that no argument returns None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_signs(self):
        """Test a list with negative and positive numbers."""
        self.assertEqual(max_integer([-3, 0, 3, -1]), 3)

    def test_zero_with_negatives(self):
        """Test a list where the max is zero."""
        self.assertEqual(max_integer([-1, 0, -2]), 0)

    def test_duplicates(self):
        """Test lists with repeated values."""
        self.assertEqual(max_integer([3, 3, 3]), 3)
        self.assertEqual(max_integer([1, 5, 5, 2]), 5)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_integers_and_floats(self):
        """Test a list that mixes integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_big_numbers(self):
        """Test a list with very big integers."""
        self.assertEqual(max_integer([10 ** 20, 5, 10 ** 21]), 10 ** 21)

    def test_strings(self):
        """Test a list of strings, which can be compared."""
        self.assertEqual(max_integer(['a', 'c', 'b']), 'c')

    def test_tuple(self):
        """Test that a tuple works like a list."""
        self.assertEqual(max_integer((1, 5, 2)), 5)

    def test_list_is_not_modified(self):
        """Test that the list is not changed by the function."""
        data = [3, 1, 2]
        max_integer(data)
        self.assertEqual(data, [3, 1, 2])

    def test_none_argument(self):
        """Test that None raises a TypeError."""
        self.assertRaises(TypeError, max_integer, None)

    def test_integer_argument(self):
        """Test that an integer instead of a list raises a TypeError."""
        self.assertRaises(TypeError, max_integer, 5)

    def test_mixed_types(self):
        """Test that numbers and strings can not be compared."""
        self.assertRaises(TypeError, max_integer, [1, "a"])
        self.assertRaises(TypeError, max_integer, ["a", 1])

    def test_none_in_list(self):
        """Test that None and numbers can not be compared."""
        self.assertRaises(TypeError, max_integer, [1, None])
        self.assertRaises(TypeError, max_integer, [None, 1])


if __name__ == "__main__":
    unittest.main()
