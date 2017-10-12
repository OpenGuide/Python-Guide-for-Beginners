"""
Interpolation search is an algorithm for searching for a given key in an
indexed array that has been ordered by numerical values assigned to the keys
(key values). It parallels how humans search through a telephone book for a
particular name, the key value by which the book's entries are ordered.
"""


def interpolation_search2(key, values):
    """
    Searches for the key using the interpolation search algorithm

    :param key: The item we want to locate
    :param values: The list of values to search. MUST be sorted.
    """
    low = 0
    high = len(values) - 1

    while (
            # There are still values in the search space
            values[low] != values[high]

            # And the key is still within the search space
            and values[low] <= key 
            and values[high] >= key):

        # Adjust the middle index to where we expect the key to be
        mid = (low +
               ((key - values[low]) * (high - low))
               // (values[high] - values[low]))

        # Adjust the bounds of the search space, depending on if the middle
        # has overshot or undershot the key
        if values[mid] < key:
            low = mid + 1
        elif values[mid] < key:
            high = mid - 1
        else:
            return mid

    if values[low] == key:
        return low
    return None

if __name__ == '__main__':
    # Test case 1: Ordered input
    key = 3
    values = list(range(0, 10))
    expected = 3
    result = interpolation_search2(key, values)
    print("Expected {}, got {}".format(expected, result))
    assert result == expected

    # Test case 2: Unordered input
    key = 8
    values = [0, 1, 3, 5, 7, 8, 12, 120, 123, 234, 456]
    expected = 5
    result = interpolation_search2(key, values)
    print("Expected {}, got {}".format(expected, result))
    assert result == expected

    # Test case 3: Not found returns None
    key = 5
    values = [2, 6, 7, 36, 42, 345]
    assert key not in values
    expected = None
    result = interpolation_search2(key, values)
    print("Expected {}, got {}".format(expected, result))
    assert result == expected
