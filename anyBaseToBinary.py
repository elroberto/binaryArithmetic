###########################################
# Algorithm to convert numbers from any base
# (where k is at least 1) to binary
# Input 1: Enter an integer base
# Input 2: Enter a comma-separated list of values
# Output: Binary value
###########################################

k = input('Enter k (2^k e.g. 3 for base 8):\n')

# Take input from command line
inputString = raw_input('Enter comma separated values:\n')
input = map(int, inputString.split(','))
input.reverse()

print "input:",input

output 	  = []
# Loop through the input values
for num in input:

	# Reset remainder value to something we can check later
	rem = -1 

	# Set exp so we can persist k if needed
	exp = k

	# Loop enough times to build a binary number out of the given input (e.g. loop count = k (power of 2)
	while exp != 0:
		exp -= 1

		# Use the remainder for calculation if not first iteration
		if rem != -1:
			num = rem

		# Integer division to find bit, remainder division to find divisor for next iteration
		bit = num  //  2**exp
		rem = num   %  2**exp

		# Store bit in list
		output.append(bit)
	
print output
