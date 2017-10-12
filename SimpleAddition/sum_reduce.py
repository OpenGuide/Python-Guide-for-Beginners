from functools import reduce

# Ask for an input of the form: int int int ... int
num = input("Space separated list of integers: -\n")

# Splits the string into numbers then uses map to convert each string into an integer
num_list = list(map(lambda x: int(x), num.split(' ')))

# Reduces the list of integers by summing them up
print(reduce((lambda x, y: x + y), num_list))

## MAP AND REDUCE ##
# Map and reduce are most commonly used in functional programming languages.

# Map applies a function to each element in a list and then returns the list
# list(map (lambda x: x * 2, [1, 2, 3, 4, 5])) => [2, 4, 6, 8, 10]

# Reduce applies a function to consecutive elements in a list in order to 'reduce'
# them to a single value. Applying this recursively to a list will eventually lead to a single data value.
# reduce((lambda x, y: x * y), [1, 2, 3, 4, 5])) => 120 as :-
# ((((1 * 2) * 3) * 4) * 5) = 120
