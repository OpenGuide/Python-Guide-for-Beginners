# fist a quick introduction about Bubble sort
# Bubble sort is a simple sorting algorithm. It repeatedly loops through the array and
# compares each pair of adjacent items and swaps them if they are in the wrong order.
# Read more at Wikipedia : https://en.wikipedia.org/wiki/Bubble_sort

# lets start with getting the user input, a random sequence of number
print "Enter numbers to be sorted (seperated by space)"
# seperating the numbers by spaces would help us in getting individual number from the input string

iplist = map(int, raw_input().split())
# raw_input() gets the sequence of numbers (seperated by space)
# split(), split the input string in individual numbers by spaces
# so if the input is "23 52 8"
# after .split() the input becomes ["23", "52", "8"]
# at the end we type cast all the string input to integers

for i in xrange( len( iplist ) ):
    for k in xrange( len( iplist )-1, i, -1 ):
        if ( iplist[k] < iplist[k-1] ):
            tmp = iplist[k]
            iplist[k] = iplist[k-1]
            iplist[k-1] = tmp

# lets break that down
# len() gives the length or the number of elements inside a list
# now we loop over the list
# as we are arranging list in ascending order
# we swap adjacent elements if they are not in order
# and we do this till all the elements are in proper order  

# fnially lets print the results
print iplist