""" Python3 Jump Search for Sorted Arrays """

import math

def jumpSearch(arr, x):
    # Define Block Size
    step = int(math.sqrt(len(arr)))

    # Finding the block where element is
    # present (if it is present)
    block = 0
    while arr[min(step*block, len(arr))] < x:
        block += 1
        if step*(block+1) > len(arr):
            break

    # Linear search for x
    linear = (block-1)*step
    while arr[linear] != x and linear < len(arr)-1:
        linear += 1
        if linear > block * step:
            return -1

    # Check to see it is value, and not just end position
    if arr[linear] == x:
        return linear
    return -1


# Example
print(jumpSearch([0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610],22))
