#!/usr/bin/env python3
"""
A Program that determines if a number is a palindrome.
A Palindrome is a word, phrase, or sequence that reads the same backward as forward.
For Example, the following items are palindromes:
    • Tenet
    • Mom
    • Bird rib
    • Racecar
    • 777
"""
import unittest


def palindrome_numbers(n: int) -> bool:
    """This function returns True if `n` is a palindrome."""
    # Change integer to a string, and compare it to its reversed string.
    return str(abs(n)) == str(abs(n))[::-1]


class TestPalindromeSolution(unittest.TestCase):
    """Tests palindrome_numbers function"""

    def setUp(self) -> None:
        """Set up test samples"""
        self.palindrome_numbers = [919, 101, 42224, 1001001, 123321, 666, 101010101, 1, 5445, 33333, 12211221]
        self.non_palindrome_numbers = [1726, 524, 8371, -920, 17779, 1110, 7721022, 1013213830, 1776, 874373822]

    def tearDown(self) -> None:
        """Teardown test samples"""
        del self.palindrome_numbers
        del self.non_palindrome_numbers

    def test_palindrome_numbers_true(self):
        """Test function to return True """
        for number in self.palindrome_numbers:
            self.assertEqual(palindrome_numbers(number), True)

    def test_non_palindrome_numbers_true(self):
        """Test function to return False"""
        for number in self.non_palindrome_numbers:
            self.assertEqual(palindrome_numbers(number), False)


if __name__ == '__main__':
    unittest.main()
