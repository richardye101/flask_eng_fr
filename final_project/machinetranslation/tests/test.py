import unittest
import translator

class TestStringMethods(unittest.TestCase):

    def test_e2f(self):
        self.assertEqual(translator.englishToFrench("Hello"), 'Bonjour')
    
    def test_f2e(self):
        self.assertEqual(translator.frenchToEnglish("Bonjour"), 'Hello')

if __name__ == '__main__':
    unittest.main()