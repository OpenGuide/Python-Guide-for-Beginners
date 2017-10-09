
def linear_search(all_items, item):
    """Searches an item inside an iterable using the
    linear search algorithm.

    Positional Arguments:
    all_items -- an iterable of items to search
    item      -- the item to find
    """
    for index, element in enumerate(all_items):
        if element == item:
            return index
    else:
        return -1


import random

# Generating a random list with 25 integers
my_list = [ random.randint(0, 100) for _ in range(25) ]
print("List: ", my_list)

# Reading the number to find in list
item_to_find = int(input("Type the number to find: "))

# Executing the linear search algorithm
found_index = linear_search(my_list, item_to_find)

# Printing the results
if found_index > -1:
    print("The {} was found at position {}!".format(item_to_find, found_index))
else:
    print("The {} wasn't found!".format(item_to_find))