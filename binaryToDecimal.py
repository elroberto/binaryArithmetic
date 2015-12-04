####################################################
# Algorithm to convert binary to decimal
# Input: string of binary digits
# Output: a vector of integers (0,1,...9) with the 
# left-most digit being the most significant
####################################################

# Set the base to 2 and the decimal value to 0
base     = 2
decimal  = 0

# Take raw input as string and map it to a list
binArr = map(int, raw_input('Enter binary:\n'))

# The exponent is the length of the string - 1
exponent = len(binArr) - 1

# Loop through the values
for num in binArr:
	# if last pass, add a 1
	if exponent == 0 and num == 1:

		decimal += 1

	# otherwise, compute the value (base^exponent + decimal)
	elif num == 1:

		decimal = base**exponent + decimal

	exponent-=1

print map(int,str(decimal))
