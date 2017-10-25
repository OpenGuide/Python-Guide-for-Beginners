def pal(n):

	s = str(n)
	for i in range(len(s)):
		if (s[i] != s[-1-i]):
			return("Not palindrome")
	
	return("Palindrome")

try:
	n = int(raw_input("Enter your number to check palindrome: "))
	print(pal(n))

except ValueError:
	print("You must enter an integer number!")

