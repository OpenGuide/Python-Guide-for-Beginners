""" Python3 Selection Sort """

unsorted = [1,54,2,34,23,3,23,32,5,34,2,23,235,324,6,43]

sorted = []
for i in range(len(unsorted)):
    sorted.append(min(unsorted[:]))
    unsorted.remove(min(unsorted[:]))

print("Sorted Array:", sorted)
