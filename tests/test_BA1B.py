import unittest
from exercises.BA1B import frequent_words

class Tests(unittest.TestCase):
    """tests for exercise BA1B"""
    
    def test_frequent_words(self):
        text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
        k = 4
        result = ["CATG", "GCAT"]
        self.assertEqual(frequent_words(text, k), result)
        
if __name__ == "__main__":
    unittest.main()
        