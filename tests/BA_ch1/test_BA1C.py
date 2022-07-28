import unittest
from exercises.BA_ch1.BA1C import reverse_complement

class Tests(unittest.TestCase):
    def test_reverse_complement(self):
        pattern = "AAAACCCGGT"
        result = "ACCGGGTTTT"

        self.assertEqual(reverse_complement(pattern), result)
        
if __name__ == "__main__":
    unittest.main()