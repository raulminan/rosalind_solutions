import unittest
from exercises import BA1K

class Tests(unittest.TestCase):
    def test_computing_frequencies(self):
        text = "ACGCGGCTCTGAAA"
        k = 2
        result = "2 1 0 0 0 0 2 2 1 2 1 0 0 1 1 0"
        
        self.assertEqual(BA1K.computing_frequencies(text, k), result)

if __name__ == "__main__":
    unittest.main()