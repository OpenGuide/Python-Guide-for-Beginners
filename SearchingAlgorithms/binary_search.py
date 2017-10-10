'''
Python 3

Binary search is a really effective search algorithm that requires the searched array to be sorted.
The basic idea is that we all the time split our array in half, and determine which half our wanted item
is located. This way, we continuously cut the area we search in half, and in the end, we will have found our
item.
'''

def binary_search(needle, haystack, low = 0, high = None):
    '''
    Searches for the needle using the binary search algorithm.
    This is a recursive implementation.
    :param needle: The item we want to locate
    :param haystack: The array in which we want to search for the needle
    :param low: The lower limit of where in the haystack we want to search.
    :param high: The upper limit of where in the haystack we want to search.
    :return: The index of the needle in the haystack, or -1 if it is not present
    '''

    # If no value for high is specified, we should search until the end of the array
    if high == None:
        high = len(haystack)

    # If the high limit is lower than the low, the haystack does not contain the needle
    if high < low:
        return -1

    # We calculate the mid point of our array (rounding it to closest integer)
    mid = int((low + high) / 2)

    if haystack[mid] > needle:
        # If the middle element is higher than the needle, we need to search the lower half of the haystack
        return binary_search(needle, haystack, low, mid - 1)
    elif haystack[mid] < needle:
        # If the middle element is lower than the needle, we need to search the upper half of the haystack
        return binary_search(needle, haystack, mid + 1, high)
    else:
        # If the middle element is neither lower or higher than the needle, the needle is located in the mid position
        return mid

if __name__ == '__main__':
    needle = 3
    haystack = [0, 1, 2, 3, 4, 5, 6, 7]
    index = binary_search(needle, haystack)
    print('The result for needle', needle, 'in haystack', haystack, 'is', index)
    
    needle = 0
    haystack = [1, 2, 3, 4, 5, 6, 7]
    index = binary_search(needle, haystack)
    print('The result for needle', needle, 'in haystack', haystack, 'is', index)