import unittest
from main import evaluarPreorder,evaluarPostorder,evaluarArbolPreorder,evaluarArbolPostorder

class Testing(unittest.TestCase):
	def test(self):
		self.assertEqual(evaluarPreorder("| & => true true false true"),"true")
		self.assertEqual(evaluarPostorder("true false => false | true false ˆ | & "),"false")
		self.assertEqual(evaluarArbolPreorder("| & => true true false true"),"True")
		self.assertEqual(evaluarArbolPostorder("true false => false | true false ˆ | &"),"False")
		
		
if __name__ == '__main__':
    unittest.main()
