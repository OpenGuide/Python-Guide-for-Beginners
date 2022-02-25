#!/usr/bin/env python3
"""
A Program that determines if a number is a Palindrome.
A Palindrome is a word, phrase, or sequence that reads the same backward as forward.
For Example, the following items are palindromes:
    • Tenet
    • Mom
    • Bird rib
    • Racecar
    • 777
"""


def palindrome_numbers(n: int) -> bool:
    """This function returns True if `n` is a palindrome."""
    # Change integer to a string, and compare it to its reversed string.
    return str(abs(n)) == str(abs(n))[::-1]
  
