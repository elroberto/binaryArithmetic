###############################################
# Algorithm that converts two numbers in any base
# and adds them up producing a number in that base.
# Input: Base, First Value, Second Value
# Output: Binary sum. 
###############################################

# Define the input values
base = input('Enter a base:\n')
x    = raw_input('Enter first value:\n')
y    = raw_input('Enter second value:\n')

# Normalize lengths
digits  = max(len(x), len(y))
x 	= x.zfill(digits)
y 	= y.zfill(digits)

# Some output
print 'input: ', x
print 'input: ', y

# Use lists and reverse them
num1 = map(int,str(x))
num2 = map(int,str(y))
num1.reverse()
num2.reverse()

sum = []

# Set iteration and carry bases
i     = 0
carry = 0

while i < digits:

	# Add previous carry (if any) to existing column value and divide by the base
	subtotal = (carry + num1[i] + num2[i]) % base

	# Set the carry using integer division
	carry 	 = (carry + num1[i] + num2[i]) // base

	sum.append(subtotal)

	i += 1

# If we carry over an extra column
if carry == 1:
	sum.append(1)

# Reverse it to human readable format
sum.reverse()

print sum
