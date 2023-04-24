"""
Script containing basic factorial algorithm.

Function uses recursion to find factorial of n.
Given a function f(n) that returns the factorial of a number:
Base case: f(0) = 1 and f(1) = 1
Recursive case: if n > 1, then f(n) = f(n-1)*n

For further reading: http://www.purplemath.com/modules/factorial.htm
https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/recursive-factorial
Advanced: https://en.wikipedia.org/wiki/Factorial
"""


def nfactorial(n):
    n = int(n)
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return nfactorial(n - 1) * n


n = input('Give n ---> ')
print(nfactorial(n))
