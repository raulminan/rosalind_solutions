import unittest
from exercises.BA_ch1.BA1A import pattern_count

class Tests(unittest.TestCase):
    def test_pattern_count(self):
        """Test for pattern_count"""
        text = "GCGCG"
        pattern = "GCG"
        result = 2

        self.assertEqual(result, pattern_count(text, pattern))
    

if __name__ == "__main__":
    unittest.main()