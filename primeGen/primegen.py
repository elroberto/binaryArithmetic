import random


class PrimeGen:

	#generate a random binary string
	def randomBinary(self,n):
		a = []
		for i in range(0,n-1):
			a.append(random.randint(0,1))
		a.append(1)
		return a

	#do modular exponentiation - necessary for large n
	def modexp(self, x, y, n):
		if y == 0: return 1
		z = self.modexp(x, y/2, n)

		if y % 2 == 0:
		     return (z * z) % n
		else:
		     return (x * z * z) % n

	#helper function for mod exp
	def modadd(self, x, y, n):
		return (x + y) % n

	#helper function for mod exp
	def modmultiply(self, x, y, n):
		return (x * y) % n

	#primality test that uses mod exp
	def primality(self,n):
		if self.modexp(3,n-1,n) == 1:
			return 1
		else:
			return 0

	#brute force primality test for less than 16 bit n
	def primalityBruteForce(self,n):
		i = 3
		while i <= n**(1/2.0):
			if n % i == 0:
				return 0
			i += 1
		return 1
			
	#decimal to binary converter	
	def decimalToBinary(self,n):
		self.sequence = []
		if n > 1:
			self.decimalToBinary(n//2)
		self.sequence.append(n % 2)
		return self.sequence

	#binary to decimal converter
	def binToDecimal(self,v):
		decimal = 0
		exponent = len(v) - 1
		for num in v:
			if exponent == 0 and num == 1:
				decimal += 1
			elif num == 1:
				decimal = 2**exponent + decimal
			exponent-=1
		return map(int,str(decimal))

	#multiply by 2 in decimal helper function
	def byTwoinDec(self,w):
		sequence = []
		for i in w:
			sequence.append(i*2)
		return sequence

	#generate n random primes and test by brute force
	#store primes into lists and output the results
	def generatePrimesBruteForce(this,n):
		primes = []
		notprimes = []
		for i in range(0,n):
			candidate = this.binToDecimal(this.randomBinary(16))
			int_value = int("".join(map(str,candidate)))
			if this.primalityBruteForce(int_value):
				primes.append(int_value)
			else:
				notprimes.append(int_value)

		print n,'digit numbers generated...'
		print 'Primes: ',len(primes)
		print 'Not primes: ',len(notprimes)

	#generate random prime of d digits  and test for primality
	#continue generating integers until one passes primality test
	def generatePrime(this,d):
		prime_generated = 0
		notprimes = [] 
		while prime_generated == 0:
			candidate = this.binToDecimal(this.randomBinary(d))
			int_value = int("".join(map(str,candidate)))
			if this.primality(int_value):
				prime_generated = 1
				print 'success with',int_value
				print len(notprimes)+1,'attempts'
				return int_value
			else:
				notprimes.append(int_value)

PrimeGen().generatePrimesBruteForce(100)
PrimeGen().generatePrime(16)
PrimeGen().generatePrime(32)
PrimeGen().generatePrime(64)
PrimeGen().generatePrime(128)
PrimeGen().generatePrime(256)
PrimeGen().generatePrime(512)

