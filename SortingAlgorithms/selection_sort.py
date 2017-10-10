def selectionSort(lst):
    """
    Selection Sort works by looping on the given list several times
    (if the length of the list is n then it loops on the list n times)
    and selecting the greatest number in the list and putting it at the
    end of the list every loop
    """
    # Lenth of the list as it will be used a lot
    length = len(lst)

    # Outer Loop
    for i in range(length):

        # Initializing the maximum number to be the first number in the list
        maxNumber = lst[0]

        # The index of the maximum number
        maxIndex = 0

        # The inner loop that searches for the greatest number
        # Note that we do not have to make it loop over the whole list
        # as the last i numbers are already sorted
        for j in range(length - i):
            if (lst[j] > maxNumber):
                maxNumber = lst[j]
                maxIndex = j

        # Now we have the index of the greatest number so we will put
        # it at the end of list but of course before the numbers that
        # we had put at the end
        lst[length - i - 1], lst[maxIndex] = lst[maxIndex], lst[length - i - 1]

    return lst

print("Please Enter a list of numbers seperated by spaces")
string = raw_input()
lst = list(map(int, string.split()))
print("The ordered list is:\n" + str(selectionSort(lst)))
