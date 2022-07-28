import pytest
from exercises.BA_ch1 import BA1F

class Tests:
    def test_BA1F_1(self):
        """Tests if it works in general
        """
        genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
        output = "11 24"
        
        assert output == BA1F.minimum_skew(genome)
    
    def test_BA1F_2(self):
        """Tests if the code indexing is off. Specifically, it verifies that the 
        code is not returning and index 1 too high or 1 too low
        """
        genome = "ACCG"
        output = "3"
        
        assert output == BA1F.minimum_skew(genome)
    
    def test_BA1F_3(self):
        """Tests if the code indexing is missing the last symbol of Genome
        """
        genome = "ACCC"
        output = "4"
        
        assert output == BA1F.minimum_skew(genome)
    
    def test_BA1F_4(self):
        """Test to make sure the minimum skew is being found, rather than the maximum
        """
        genome = "CCGGGT"
        output = "2"
        
        assert output == BA1F.minimum_skew(genome)
    
    def test_BA1F_5(self):
        """Checks if only 1 index is being found and if a delimiter (space) is being
        used to separate indices
        """
        genome = "CCGGCCGG"
        output = "2 6"
        
        assert output == BA1F.minimum_skew(genome)