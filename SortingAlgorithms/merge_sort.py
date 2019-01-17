
def mergeSort(listToSort):
	if(len(listToSort) > 1):
		mid = len(listToSort)//2
		lower = listToSort[:mid]
		upper = listToSort[mid:]

		mergeSort(lower)
		mergeSort(upper)

		i = 0
		j = 0
		k = 0
		while(i < len(lower) and j < len(upper)):
			if(lower[i] < upper[j]):
				listToSort[k] = lower[i]
				i = i + 1
			else:
				listToSort[k] = upper[j]
				j = j + 1
			k = k + 1

		while(i < len(lower)):
			listToSort[k] = lower[i]
			i = i + 1
			k = k + 1

		while(j < len(upper)):
			listToSort[k] = upper[j]
			j = j + 1
			k = k + 1

print "Enter numbers to be sorted (separated by space)"

userList = map(int, raw_input().split())
mergeSort(userList)

print userList
