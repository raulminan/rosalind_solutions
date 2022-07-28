import unittest
import pytest

from exercises.BA_ch1 import BA1E

class Tests:
    def test_find_clumps_frequent_words(self):
        genome = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
        k = 5
        L = 75
        t = 4
        result = "CGACA GAAGA AATGT"
        
        self.assertEqual(BA1E.find_clumps_frequent_words(genome, k, L, t), result)
    
    def test_clump_finding(self):
        genome = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
        k = 5
        L = 75
        t = 4
        result = "CGACA GAAGA AATGT"
        
        self.assertEqual(BA1E.clump_finding(genome, k, L, t), result)
        
    def test_better_clump_finding_1(self):
        """General test to see if it works"""
        
        genome = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
        k = 5
        L = 75
        t = 4
        result = ["CGACA", "GAAGA", "AATGT"]
        
        assert set(result) == set(BA1E.better_clump_finding(genome, k, t, L))
    
    def test_better_clump_finding_2(self):
        """Test to make sure the code only counts k-mers that fall completely
        within a L-window"""
        
        genome = "AAAACGTCGAAAAA"
        k, L, t = 2, 4, 2
        result = ["AA"]
        
        assert set(result) == set(BA1E.better_clump_finding(genome, k, t, L))
        
    def test_better_clump_finding_3(self):
        """Checks if the code has an off-by-one error when checking k-mers within
        an L-window."""
        
        genome = "ACGTACGT"
        k, L, t = 1, 5, 2
        result = ["A", "C", "G", "T"]
        
        assert set(result) == set(BA1E.better_clump_finding(genome, k, t, L))
        
    def test_better_clump_finding_4(self):
        """Checks if the code is correctly handling overlapping k-mers"""
        
        genome = "CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG"
        k, L, t = 3, 25, 3
        result = ["AAA", "CAG", "CAT", "GCC", "TTC"]
        
        assert set(result) == set(BA1E.better_clump_finding(genome, k, t, L))
        
    def test_better_clump_finding_small(self):
        short_genome = "GATCAGCATAAGGGTCCCTGCAATGCATGACAAGCCTGCAGTTGTTTTAC"
        short_k = 4
        short_t = 3
        short_L = 25
        short_result = ["TGCA"]
        
        assert set(short_result) == set(BA1E.better_clump_finding(short_genome, short_k, short_t, short_L))
        
   