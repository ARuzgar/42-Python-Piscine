"""
Test suite for ft_package.utils module.
"""

import unittest
from ft_package import count_in_list, reverse_list


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""

    def test_count_in_list(self):
        """Test the count_in_list function."""
        self.assertEqual(count_in_list(["toto", "tata", "toto"], "toto"), 2)
        self.assertEqual(count_in_list(["toto", "tata", "toto"], "tutu"), 0)
        self.assertEqual(count_in_list([], "any"), 0)
        self.assertEqual(count_in_list(["a", "b", "c", "a"], "a"), 2)

    def test_reverse_list(self):
        """Test the reverse_list function."""
        self.assertEqual(reverse_list(["a", "b", "c"]), ["c", "b", "a"])
        self.assertEqual(reverse_list([]), [])
        self.assertEqual(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()