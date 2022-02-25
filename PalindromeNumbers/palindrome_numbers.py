#!/usr/bin/env python3
"""created:02-24-2022 22:46:02, author:seraph★776, project: Palindrome Numbers.

A Palindrome is a word, phrase, or sequence that reads the same backward as forward.
For Example, the following items are palindromes:
    - Tenet 
    - Bird rib
    - Racecar
    - Mom
   
This program will determine if a given integer is a palindrome number (i.e. 777, 1001001, 666, etc,.)
"""


def palindrome_numbers(n: int) -> bool:
    """This function returns True if `n` is a palindrome."""
    # Change integer to a string, and compare it to its reversed string.
    # Use `abs()` method to account for negative integers.
    return str(abs(n)) == str(abs(n))[::-1]
