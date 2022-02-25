#!/usr/bin/env python3
"""created:02-24-2022 22:46:02, author:seraph★776, project: Palindrome Numbers Test."""

import unittest
from palindrome_numbers import palindrome_numbers


class TestPalindromeSolution(unittest.TestCase):
    """Tests palindrome_numbers function"""

    def setUp(self) -> None:
        self.palindrome_numbers = [919, 101, 42224, 1001001, 123321, 666, 101010101, 1, 5445, 33333, 12211221]
        self.non_palindrome_numbers = [1726, 524, 8371, -920, 17779, 1110, 7721022, 1013213830, 1776, 874373822]

    def tearDown(self) -> None:
        del self.palindrome_numbers
        del self.non_palindrome_numbers

    def test_palindrome_numbers_true(self):
        for number in self.palindrome_numbers:
            self.assertEqual(palindrome_numbers(number), True)

    def test_non_palindrome_numbers_true(self):
        for number in self.non_palindrome_numbers:
            self.assertEqual(palindrome_numbers(number), False)


if __name__ == '__main__':
    unittest.main()
