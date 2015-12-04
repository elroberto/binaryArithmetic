#binaryArithmetic
Python code for number conversions and some simple arithmetic

##binaryToDecimal.py
Input a binary input string and convert it to a decimal. The input string is fed into a list container, which is then looped. Each decimal digit is calculated and summed. If the loop is on its last pass and we still have a decimal value, add 1 digit.

##anyBaseToBinary.py
Input (1) a power of 2 (e.g. 3 for base 8) and (2) a comma-separated list of values. The values are read into a list, reversed, then calculated into binary. The binary calculation involves two loops. Loop one is to iterate through the array values. Loop two is to calculate the binary values of the integer using division by the value of a given bit (e.g. place 0 = 2^0, place 1 = 2^1, etc.).

##addTwo.py
Input (1) is the base to be added, (2) is the first number and (3) the second. Numbers to be added are padded to the same length and added to respective lists. A for loop iterates through the digits doing simple arithmetic row by row.

##numbers.py
This file includes functions that support problems one through three. This file is not called directly, but included at the top of each of the files listed below. In this file, I implemented iterative versions of all three algorithms and attempted a recursive division algorithm, but couldn’t get the code to pass validation.

##subtractTwoAnyBase.py
Call this from the command line with python subtractTwoAnyBase.py. You will be prompted for two numbers entered as strings and a base value.

##multiplyTwo.py
Call this from the command line with python multiplyTwo.py. You will be prompted for two numbers entered as strings and a base value.

#Prime Number Generation
##generate a random binary string
randomBinary(self,n):
  
##do modular exponentiation - necessary for large n
modexp(self, x, y, n):
  
##helper function for mod exp
modadd(self, x, y, n):
  
##helper function for mod exp
modmultiply(self, x, y, n):

##primality test that uses mod exp
primality(self,n):

##brute force primality test for less than 16 bit n
*tests divisors up to sqrt(n)*
primalityBruteForce(self,n):

##decimal to binary converter    
decimalToBinary(self,n):

##binary to decimal converter
binToDecimal(self,v):

##multiply by 2 in decimal helper function
byTwoinDec(self,w):

##generate n random primes and test by brute force
*store primes into lists and output the results*
generatePrimesBruteForce(this,n):

##generate random prime of d digits  and test for primality
*continue generating integers until one passes primality test*
generatePrime(this,d):

##Instructions for running the Primegen code:

* Run the command ```python – m primegen```  in the same directory as primegen.py. All tests are setup to run at the end of the file. 
* Run the command ```python –m unittest tests``` in the same directory as tests.py to run unit tests. I used this throughout the development to ensure code did not break along the way. 

## Example
###Brute force
To test my algorithm for 16-bit integer, I called generatePrimesBruteForce(100).  Generally speaking, only between 10 and 25 of the 16 bit numbers generated were prime. 

###Generating Primes
I then used by algorithm three times to generate 16, 32, 64, 128, 256, and 512 digit numbers. Here is the report. The first column is the length of the number, the second through fourth columns are the number of tries it took to generate the prime. 



