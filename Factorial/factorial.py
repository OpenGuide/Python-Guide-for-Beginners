def factorial_recursive(n):
    """Returns the factorial of n using a recursive function"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial(n):
    """Returns the factorial of n"""
    return reduce(lambda x, y: x * y, (x for x in xrange(1, n + 1)))


n = input("Please enter the a number: ")
print "Factorial of the number is %d" % factorial(n)
