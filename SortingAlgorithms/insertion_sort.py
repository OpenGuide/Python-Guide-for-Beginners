def insertion_sort(values):
    # Note: Almost always, iterating over an array in python is done by loops in the form
    #   for element in array:
    # or
    #   for (index, element) in enumerate(array):
    # however, since insertion sort is based on index manipulation, the loop style
    #   for index in range(len(array)):
    #       element = array[index]
    # is used here.
    for i in range(1, len(values)):
        value1 = values[i]
        # In this loop, we know that the first i values are already in correct order
        # (note that in the first iteration i = 0)
        # In the next loop, we will insert value1 at the correct position in these i values.
        # range(i-1, -1, -1) counts down from i-1 to 0
        for j in range(i-1, -1, -1):
            value2 = values[j]
            # Are these two elements in the wrong order? If so, swap them.
            if value1 < value2:
                # This is the idiomatic way to swap two elements in python
                values[j+1], values[j] = values[j], values[j+1]
            # Otherwise we are done since we have inserted value1 in the correct position
            else:
                break
    return values
