# pad two lists to the same number of digits
def listFill(x,y):
	len_x = len(x)
	len_y = len(y)

	columns = max(len_x,len_y)

	if len_x < columns:
		for z in range(0,columns-len_x):		
			x.append(0)
	if len_y < columns:
		for z in range(0,columns-len_y):		
			y.append(0)
	return x,y

# divide by two in binary	
def divideByTwo(x):
	if x == []:
		return []
	x.reverse() 
	x.pop() 
	x.reverse() 
	return x

# multiply by two in binary	
def multiplyByTwo(x):
	if x == [] or x == 0:
		return []
	x.reverse() 
	x.append(0)
	x.reverse() 
	return x
	
#determine if a binary number is odd
def isOdd(x):
	if x == []:
		return False

	x.reverse() 
	
	return x[-1] != 0

# subtract two numbers of any base 2^k
def subtract(num1,num2,base):
	if num2 == []:
		return num1

	num1,num2 = listFill(num1,num2)

	digits  = max(len(num1), len(num2))
	d       = []

	# Set iteration and carry bases
	i        = 0
	borrowed = 0

	while i < digits:

		# If we borrowed, deduct it
		if (borrowed == 1): 
			num1[i] = num1[i] - 1

		# If top is greater, we can make our subtraction
		if (num1[i] >= num2[i]):
			d.append((num1[i]) - num2[i])
			borrowed = 0

		# Otherwise, we need to borrow from the next column (base value)
		else:
			d.append(base + (num1[i] - num2[i]))
			borrowed = 1
				
		i += 1

	return d

# add two numbers of any base 2^k
def add(x,y,base):
	x,y = listFill(x,y)	
	columns = len(x)
	
	sum    = []

	# Set iteration and carry bases
	i     = 0
	carry = 0

	while i < columns:

		# Add previous carry (if any) to existing column value and divide by the base
		subtotal = (carry + x[i] + y[i]) % base

		# Set the carry using integer division
		carry 	 = (carry + x[i] + y[i]) // base

		sum.append(subtotal)

		i += 1

	# If we carry over an extra column
	if carry == 1:
		sum.append(1)

	return sum

# multiply two numbers of any base 2^k
def multiply(num1,num2,base=2):
	
	if num1 == [] or num2 == []:
		return []

	# Normalize lengths
	digits  = max(len(num1), len(num2))

	i = 0
	tot = []

	# loop through all digits in number
	while i < digits:
		x     = 0
		sub   = [] 
		carry = 0

		# append appropriate amount of zeros
		for s in range(0,i):
			sub.append(0)

		# loop through and multiply the bottom digit by each of the top digits
		# also set the carry
		# do this in a way that is base 2^k friendly
		while x < digits:
			product = num2[i] * num1[x]
			sub.append((product + carry) % base)
			carry = (product + carry) // base
			x += 1
		
		# if we still have a carry, add it to the total
		if (carry > 0):
			sub.append(carry)

		i += 1

		tot.append(sub)

	sum = []
	tot_length = len(tot)

	# now we have a lists of lists that contain the products of the multiplication
	# loop through these and add them up 
	for z in range(0,tot_length):
		sum = add(sum,tot.pop(),base)
		
	return sum

# divide two numbers of any base 2^k
# only supports one base
def itdivide(x,y,base=2):
	q = 0
	r = 0

	for i in range(0,len(x)-1):
		q = multiplyByTwo(q)
		r = multiplyByTwo(r)

		if x[i] == 1:
			r = add(r,[1],base)

		if r >= y:
			r = subtract(r,y,base)
			q = add(q,[1],base)
	return q,r

# implemented the recursive version of division algorithm, but couldn't get it to pass validation
def divide(x,y,base=2):
	if x == []:
		return ([0],[0])

	q,r = divide(divideByTwo(x),y)

	q = multiplyByTwo(q)
	r = multiplyByTwo(r)

	if isOdd(x):
		r = add(r,[1])

	if r >= y:
		r = subtract(r,y)
		q = add(q,[1])

	return q,r
