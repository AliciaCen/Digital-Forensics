import sys

# allows you to be able to read from the stdin and sets that to a variable
b = sys.stdin.read()
# sets the string for the final statement
words = ''

# Checks to see if the length of b is divisible by 7
if (len(b)-1) % 7 == 0:
	# continues loop until the end of the page excluding the new line. 
	while len(b) > 7:
		# sets variable to the first 7 digits
		seven = b[0:7]
		# re-defines b so that it no longer includes the first seven digits you read
		b = b[7:len(b)]
		# changes the characters to binary
		int(seven, 2)
		# changes the binary number to a base 10 number then changes the number to a letter and saves it to a variable
		letter = chr(int(seven, 2))
		# Adds the letter to the string
		words += letter
	# prints the string when the loop is done. 
	print words		

# Checks to see if the length of b is divisible by 8
elif (len(b)-1) % 8 == 0:
	# continues loop until the end of the page excluding the new line. 
	while len(b) > 8:
		# sets variable to the first 7 digits
		eight = b[0:8]
		# re-defines b so that it no longer includes the first eight digits you read
		b = b[8:len(b)]
		# changes the characters to binary
		int(eight, 2)
		# changes the binary number to a base 10 number then changes the number to a letter and saves it to a variable
		letter = chr(int(eight, 2))
		# Adds the letter to the string
		words += letter
	# prints the string when the loop is done. 
	print words		

# Tells you that the number of characters is not divisible by 7 or 8 and it cannot read that binary. 
else:
	print "The amount of characters in your file does not go in evenly to 7 or 8"