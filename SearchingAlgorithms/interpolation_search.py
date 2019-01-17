# Interpolation search (https://en.wikipedia.org/wiki/Interpolation_search)

# Interpolation search is an improved variant of binary search. 
# This search algorithm works on the probing position of the required value.
# For this algorithm to work properly, the data collection should be in a sorted form and equally distributed.

# Steps taken to search for index of the target value using probing.
# Step 1 - Start searching data from middle of the list.
# Step 2 - If it is a match, return the index of the item, and exit.
# Step 3 - If it is not a match, probe position.
# Step 4 - Divide the list using probing formula and find the new midle.
# Step 5 - If data is greater than middle, search in higher sub-list.
# Step 6 - If data is smaller than middle, search in lower sub-list.
# Step 7 - Repeat until match.

from random import randrange


def interpolation_search(sorted_list, to_find):
	# Lower bound start position.
	low = 0

	# Higher bound start position.
	high = len(sorted_list) -1

	# While we haven't ran out of items to check.
	while low <= high and to_find >= sorted_list[low] and to_find <= sorted_list[high]:

		# Calculate middle position with probing.
		# high - Highest index of the list.
		# low - Lowest index of the list.
		middle_position = low + int(((float(high - low) / (sorted_list[high] - sorted_list[low])) * (to_find - sorted_list[low])))

		# Element found.
		if sorted_list[middle_position] == to_find:
			return middle_position

		if to_find > sorted_list[middle_position]:
			# Seeked value is higher than middle value, move the lower end of the probe over the middle position.
			low = middle_position + 1
		else:
			# Seeked value is lower than middle value, decrease the high end of the probe below the middle position.
			high = middle_position - 1

	# Value not found.
	return None


if __name__ == '__main__':
	# Generate sorted list of 1000 values, ranging from 0 to 999.
	sorted_list = sorted(list(range(1000)))
	# Randomly select one value between 0 and 999
	to_find = randrange(1000)
	# Use interpolation search to find selected value from list.
	result = interpolation_search(sorted_list, to_find)

	# Print result of the search.
	if result is None:
		print("Could not find value " + str(to_find))
	else:
		print("Found value " + str(to_find) + " at index " + str(result) + " from list with values from 0 to " + str(len(sorted_list)))