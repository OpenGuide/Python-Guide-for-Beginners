'''
This program uses Map reduce techniques to get sum of numers.
How it works:
We first call the mapper.py that prints the relevent data to the terminal.

Then the reducer is called that prints out the sum of the numbers.
This is just a very basic example that will not be of much use.
But if you have gigabytes of numbers ot add , you cna run it with hadoop streaming.
'''
#!/usr/bin/env python

import sys

def mapper():
	# Read input line
	for line in sys.stdin:
		# Strip off whitespace , and split on tab
		data = line.strip().split('\t')

		# We'll use the data stored in data/mapreduce/
		# Having six columns of tab seperated values
		# We'll make sure that correct data in sent through
		print data
		if len(data) ==2:
			sr , num = data

			# Now we'll print our data as required for the reducer task
			# I need category and cost so we'll print that
			print "{0}".format(num)

mapper()

'''

# Testing :

test_data = """1  54
2 64
3 1
"""

def main():

	# Used for testing the mapper function

	import StringIO
	sys.stdin = StringIO.StringIO(test_data)
	mapper()
	sys.stdin = sys.__stdin__

'''

def reducer():
	# Following the mapper.py , we need to get total
	# sum.
	Total = 0 

	for line in sys.stdin:
		
		data = line.strip().split("\t")

		# Our mapper gives out 2 values

		if len(data) != 1:
			# This keeps check of the data errors
			continue

		thisnum = data 
		Total += float(thisnum)

	print Total


# Calling the reducer function

#reducer()
