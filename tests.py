import unittest
from main import evaluarPreorder,evaluarPostorder,evaluarArbolPreorder,evaluarArbolPostorder

class Testing(unittest.TestCase):
	def test(self):
		self.assertEqual(evaluarPreorder("| & => true true false true"),"true")
		self.assertEqual(evaluarPostorder("true false => false | true false ˆ | & "),"false")
		self.assertEqual(evaluarArbolPreorder("| & => true true false true"),"True")
		self.assertEqual(evaluarArbolPostorder("true false => false | true false ˆ | &"),"False")
		self.assertEqual(evaluarPreorder("& & true | false true false"),"false")
		self.assertEqual(evaluarArbolPreorder("& & true | false true false"),"False")
		self.assertEqual(evaluarPostorder("true false true | & false &"),"false")
		self.assertEqual(evaluarArbolPostorder("true false true | & false &"),"False")
		self.assertEqual(evaluarPreorder("& ^ true false"),"false")
		self.assertEqual(evaluarArbolPreorder("& ^ true false"),"False")
		self.assertEqual(evaluarPostorder("true ^ false &"),"false")
		self.assertEqual(evaluarArbolPostorder("true ^ false &"),"False")
		
		self.assertEqual(evaluarPreorder("& true false"),"false")
		self.assertEqual(evaluarArbolPreorder("& true false"),"False")
		self.assertEqual(evaluarPreorder("| true false"),"false")
		self.assertEqual(evaluarArbolPreorder("| true false"),"False")
		self.assertEqual(evaluarPreorder("& true true"),"true")
		self.assertEqual(evaluarArbolPreorder("& true true"),"True")
		self.assertEqual(evaluarPreorder("| false false"),"false")
		self.assertEqual(evaluarArbolPreorder("| false false"),"False")
		self.assertEqual(evaluarPreorder("| true true"),"true")
		self.assertEqual(evaluarArbolPreorder("| true true"),"True")
		self.assertEqual(evaluarPreorder("& false true"),"false")
		self.assertEqual(evaluarArbolPreorder("& false true"),"False")
		self.assertEqual(evaluarPreorder("| false true"),"true")
		self.assertEqual(evaluarArbolPreorder("| false true"),"True")
		self.assertEqual(evaluarPreorder("=> true false"),"false")
		self.assertEqual(evaluarArbolPreorder("=> true false"),"False")
		self.assertEqual(evaluarPreorder("=> false true"),"true")
		self.assertEqual(evaluarArbolPreorder("=> false true"),"True")
		self.assertEqual(evaluarPreorder("=> false false"),"true")
		self.assertEqual(evaluarArbolPreorder("=> false false"),"True")
		
if __name__ == '__main__':
    unittest.main()
