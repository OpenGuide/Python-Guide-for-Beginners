# A quick intro to Insertion sort
# It is sorting algorithm that builds the final sorted list one item at a time.
# At each iteration, insertion sort removes one element from the input data, 
# finds its proper location within the sorted list, and inserts it there.
# Read more at Wikipedia : https://en.wikipedia.org/wiki/Insertion_sort

# lets get the user input
print "Enter numbers to be sorted (seperated by space)"

iplist = map(int, raw_input().split())
# for detailed explanation look up at bubble_sort.py

for index in xrange( 1, len(iplist) ):
    currentvalue = iplist[index]
    position = index

    while ( position > 0 and iplist[position-1] > currentvalue ):
        iplist[position] = iplist[position-1]
        position = position - 1

    iplist[position] = currentvalue

print iplist
