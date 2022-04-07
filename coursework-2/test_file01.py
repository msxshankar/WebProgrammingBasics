import unittest
import file01 as f1

class Test(unittest.TestCase):

	def test_check_key(self):
		self.assertFalse(f1.check_key(-1))
		self.assertTrue(f1.check_key(0))
		self.assertTrue(f1.check_key(1))
		self.assertTrue(f1.check_key(50))
		self.assertTrue(f1.check_key(94))
		self.assertFalse(f1.check_key(95))
		self.assertFalse(f1.check_key('a'))

	def test_check_upper_lower(self):
		self.assertListEqual(f1.check_upper_lower('The quick Brown Fox!'), [3, 13])
		self.assertListEqual(f1.check_upper_lower('Khoor#Zruog#=,'), [2, 8])
		self.assertListEqual(f1.check_upper_lower('012345'), [0, 0])
				
	def test_encrypt_decrypt_string(self):
		self.assertEqual(f1.encrypt_decrypt_string("Hello World :)"), "Khoor#Zruog#=,")
		self.assertEqual(f1.encrypt_decrypt_string("Khoor#Zruog#=,",3,2), "Hello World :)")
		self.assertEqual(f1.encrypt_decrypt_string("Khoor#Zruog#=,",option = 2), "Hello World :)")
		self.assertEqual(f1.encrypt_decrypt_string("Hello World :)", key = 100), "Invalid key!")
		self.assertEqual(f1.encrypt_decrypt_string("Hello World :)", option = 4), "Invalid option!")
		
	def test_count_words_in_file(self):
		self.assertEqual(f1.count_words_in_file('test1.txt'), {'HELLO': 1, 'WORLD': 2, 'HOW': 1, 'ARE': 1, 'YOU': 1, 'DOING': 1, 'I': 1, 'LOVE': 1, 'THIS': 1})
		self.assertEqual(f1.count_words_in_file('test2.txt'), {'TEST': 3, 'ONE': 2, 'TWO': 1, 'THREE': 1})
		self.assertEqual(f1.count_words_in_file('test3.txt'), "Wrong file or file path")
		
	def test_summarise_data(self):
		self.assertEqual(f1.summarise_data("traffic_data.txt", 0), [13096, 6493, 471876, 50, 9437.52])
		self.assertEqual(f1.summarise_data("traffic_datatxt", 1), [11799, 5778, 421298, 50, 8425.96])
		self.assertEqual(f1.summarise_data("population_10.txt", 5), [1371851, 1730, 3327840, 34, 97877.65])
		self.assertEqual(f1.summarise_data("population_10.txt", 6), [1425791, 1878, 4274491, 38, 112486.61])
		self.assertEqual(f1.summarise_data("filenotexist.txt", 0), "FileNotFoundError")
				

