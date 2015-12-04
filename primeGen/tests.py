import unittest
import random
from primegen import PrimeGen

class TestPrimeGen(unittest.TestCase):

	def setUp(self):
		self.seq = range(10)
		self.testNumber = random.choice(self.seq)

	def test_random_binary_is_list(self):
		primegen = PrimeGen()
		result = primegen.randomBinary(1)
		self.assertNotIsInstance(result,basestring)
	
	def test_random_binary_most_significant_one(self):
		primegen = PrimeGen()
		result = primegen.randomBinary(4)
		self.assertEqual(result[-1],1)

	def test_random_binary_all_digits_binary(self):
		primegen = PrimeGen()
		result = primegen.randomBinary(4)
		for i in result:
			self.assertIn(result[i],[0,1])

	def test_mod_add(self):
		primegen = PrimeGen()
		result = primegen.modadd(123456789,987654321,7)
		self.assertEqual(result,4)

	def test_mod_multiply(self):
		primegen = PrimeGen()
		result = primegen.modmultiply(585,1609,7)
		self.assertEqual(result,3)

	def test_mod_exp(self):
		primegen = PrimeGen()
		result = primegen.modexp(10,2,90)
		self.assertEqual(result,10)

	def test_primality(self):
		primegen = PrimeGen()
		result = primegen.primality(193)
		self.assertEqual(result,1)

	def test_decimalToBinary(self):
		primegen = PrimeGen()
		result = primegen.decimalToBinary(1609)
		self.assertEqual(result,[1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1])

	def test_byTwoinDec(self):
		primegen = PrimeGen()
		result = primegen.byTwoinDec([2,6,12,24,15])
		self.assertEqual(result,[4,12,24,48,30])

	def test_binToDecimal(self):
		primegen = PrimeGen()
		result = primegen.binToDecimal([1,0,0,0,1,0,0,1])
		self.assertEqual(result,[1,3,7])

suite = unittest.TestLoader().loadTestsFromTestCase(TestPrimeGen)
unittest.TextTestRunner(verbosity=2).run(suite)
		
