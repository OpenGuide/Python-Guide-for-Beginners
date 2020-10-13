def floyds_triangle(n):
    """
        Print Floyds Triangle for given n
    """
    r = 1
    for i in xrange(1, n + 1):
        print ' '.join(str(i) for i in xrange(r, i + r))
        r += i


n = input("Enter a number: ")
floyds_triangle(n)
