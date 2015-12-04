from numbers import *

# Define the input values
base = input('Enter a base:\n')
x    = raw_input('Enter first value:\n')
y    = raw_input('Enter second value:\n')

# Normalize lengths
digits  = max(len(x), len(y))
x 	= x.zfill(digits)
y 	= y.zfill(digits)

if y == 0:
	print 'Multipying by zero value is 0'
	raise SystemExit

# Some output
print 'input: ', x
print 'input: ', y

# Use lists and reverse them
num1 = map(int,str(x))
num2 = map(int,str(y))
num1.reverse()
num2.reverse()

print multiply(num1,num2,base)
