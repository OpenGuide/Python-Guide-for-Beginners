def quicksort(values):
    if len(values) <= 1:
        return values
    # Choose an element from the list
    # This choice is almost arbitrary. However, choosing the first element of the list
    # can lead to worst-case behavior for an already sorted list so we'll use the middle element
    pivot = values[len(values) // 2]
    # Split the list into those elements that are smaller than the pivot element and those that are larger
    smallerElements = [value for value in values if value < pivot] 
    largerElements = [value for value in values if value > pivot]
    # Sort each of these smaller lists individually and then concatenate them in the right order
    return quicksort(smallerElements) + [pivot] + quicksort(largerElements)
