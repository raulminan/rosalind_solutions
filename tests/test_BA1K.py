import unittest
from exercises import BA1K

class Test:
    def test_computing_frequencies(self):
        """Test general case"""
        text = "ACGCGGCTCTGAAA"
        k = 2
        correct_output = "2 1 0 0 0 0 2 2 1 2 1 0 0 1 1 0"
        result = BA1K.computing_frequencies(text, k, output_str=True)
        assert result == correct_output
        
    def test_computing_frequencies_2(self):
        """Tests if theres off-by-one error at the end of text"""
        text = "AAAAC"
        k = 2
        correct_output = "3 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
        result = BA1K.computing_frequencies(text, k, output_str=True)
        assert result == correct_output

    def test_computing_frequencies_3(self):
        """Tets if theres and off-by-one error at the beggining of text"""
        text = "TTAAA"
        k = 2
        correct_output = "2 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1"
        result = BA1K.computing_frequencies(text, k, output_str=True)
        assert result == correct_output

    def test_computing_frequencies_4(self):
        """Tests if the code is actually updating the count"""
        text = "AAA"
        k = 2
        correct_output = "2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
        result = BA1K.computing_frequencies(text, k, output_str=True)
        assert result == correct_output