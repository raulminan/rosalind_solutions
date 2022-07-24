import unittest
from exercises.BA1D import find_occurences

class Tests(unittest.TestCase):
    def test_find_occurences(self):
        pattern = "ATAT"
        genome = "GATATATGCATATACTT"
        result = "1 3 9"

        self.assertEqual(find_occurences(pattern, genome), result)

if __name__ == "__main__":
    unittest.main()