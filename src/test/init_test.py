import unittest
import sys
sys.path.insert(0, '../../src')
import init_python

class TestInitPython(unittest.TestCase):
	def test_caps_string(self):
		self.assertEqual(init_python.caps_string('fOO'), 'FOO')



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestInitPython)
    unittest.TextTestRunner(verbosity=2).run(suite)



