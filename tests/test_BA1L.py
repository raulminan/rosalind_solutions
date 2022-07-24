import unittest
from exercises import BA1L

class Tests(unittest.TestCase):
    def test_pattern_to_number(self):
        pattern = "AGT"
        result = 11
        
        self.assertEqual(BA1L.pattern_to_number(pattern), result)

if __name__ == "__main__":
    unittest.main()
        