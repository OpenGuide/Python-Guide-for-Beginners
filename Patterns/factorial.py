
print "Enter a number to get factorial."
userInput = map(int, raw_input().split())

i = 1
answer = 1
if(userInput[0] != 0):
	while(i <= userInput[0]):

		tmp = answer
		answer = i * tmp
		i = i + 1

print answer

