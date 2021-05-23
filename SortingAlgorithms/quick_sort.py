# 'Quick Sort'
# Randomize Pivot to avoid worst case, currently pivot is last element


def quickSort(A, si, ei):
    if si < ei:
        pi = partition(A, si, ei)
        quickSort(A, si, pi-1)
        quickSort(A, pi+1, ei)


# 'Partition'
# Utility function for partitioning the array(used in quick sort)
def partition(A, si, ei):
    x = A[ei]  # x is pivot, last element
    i = (si-1)
    for j in range(si, ei):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            A[i+1], A[ei] = A[ei], A[i+1]      
    return i+1


# Alternate Implementation
# Warning --> As this function returns the array itself, assign it to some
# Variable while calling. Example--> sorted_arr=quicksort(arr)  
# 'Quick sort'


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) / 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
