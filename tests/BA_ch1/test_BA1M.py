import unittest
from exercises.BA_ch1 import BA1M

class Tests(unittest.TestCase):
    def test_number_to_pattern(self):
        index = 45
        k = 4
        result = "AGTC"
        
        self.assertEqual(BA1M.number_to_pattern(index, k), result)

if __name__ == "__main__":
    unittest.main()