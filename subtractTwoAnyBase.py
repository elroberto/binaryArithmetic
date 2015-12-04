from numbers import *

# Define the input values
base = input('Enter a base (e.g. 2^k (2 for base 2, 8 for base 8):\n')
x    = raw_input('Enter first value:\n')
y    = raw_input('Enter second value:\n')


# Normalize lengths
digits  = max(len(x), len(y))
x 	= x.zfill(digits)
y 	= y.zfill(digits)

if y > x:
	print 'Error: Your second integer is larger, cannot compute\r'
	raise SystemExit

if y == x:
	print 'Values are equal'
	raise SystemExit

# Some output
print 'input: ', x
print 'input: ', y

# Use lists and reverse them
num1 = map(int,str(x))
num2 = map(int,str(y))
num1.reverse()
num2.reverse()

print subtract(num1,num2,base)
