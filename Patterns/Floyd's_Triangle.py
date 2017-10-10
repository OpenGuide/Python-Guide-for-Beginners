from __future__ import print_function

def floyds_triangle(n):
    """
    This method prints Floyd's triangle which is a right-angled
    triangular array of natural numbers. Defined by filling the rows
    of the triangle with consecutive numbers, starting with a 1 in the
    top left corner. (Source description: Wikipedia.org)
    
    :param n: The amount of rows
    """
    
    number = 1
    
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(number, " ", end="\t")
            number += 1

        print()
