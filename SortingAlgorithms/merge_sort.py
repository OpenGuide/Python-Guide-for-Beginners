# Mergesort: Introduction
# Merge sort is a recursive algorithm that continually splits a list in half. 
# If the list is empty or has one item, it is sorted by definition (The base case)
# If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. 
# Once the two halves are sorted, the fundamental operation, called a merge, is performed. 
# Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list. 

print "MERGE SORT"
print "Enter numbers to be sorted (seperated by space)"


# Ask the user to input to input values and split them from spaces.
iplist = map(int, raw_input().split())


# Merge routine for left and right side of the array.
def merge(left, right):
    # Sorted array to be filled and returned.
    sorted_array = []

    # Run as long as either side runs out of values.
    while len(left) > 0 and len(right) > 0:
        # Check which of the first values is smaller
        # and append the resulting array with the value
        # while removing the value from the original array. 
        if left[0] < right[0]:
            sorted_array.append(left.pop(0))
        else:
            sorted_array.append(right.pop(0))


    # Ran out of numbers in either side.
    # Extend the resulting array with the remaining values 
    # from the array that has values.
    if len(left) == 0:
        sorted_array.extend(right)
    else:
        sorted_array.extend(left)

    # Return the sorted array.
    return sorted_array


# Merge sort runs recursively. 
# Takes presumably unsorted array as paramter.
def mergesort(unsorted_list):

    # If size of the list is less than or equal to 1, the list is already sorted. (The base case)
    if len(unsorted_list) <= 1:
        return unsorted_list

    # Get the middle point of the array where it's going to get splitted.
    middle = len(unsorted_list) / 2

    # Left side of the unsorted array that is getting sorted.
    left = mergesort(unsorted_list[:middle])

    # Right side of the unsorted array that is getting sorted.
    right = mergesort(unsorted_list[middle:])

    # Merge left side with right side.
    return merge(left, right)


# Print the result.
print(mergesort(iplist))
