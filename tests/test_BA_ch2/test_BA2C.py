from exercises.BA_ch2 import BA2C

class Tests():
    def test_find_probable_kmer(self):
        """General case"""
        
        k = 5
        text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
        profile = [
            [0.2, 0.2, 0.3, 0.2, 0.3],
            [0.4, 0.3, 0.1, 0.5, 0.1],
            [0.3, 0.3, 0.5, 0.2, 0.4],
            [0.1, 0.2, 0.1, 0.1, 0.2]
        ]
        
        correct_output = "CCGAG"
        result = BA2C.find_profile_probable_kmer(text, k, profile)
        
        assert correct_output == result
    
    def test_off_by_one_beginning(self):
        """This dataset checks for off-by-one errors at the beginning of Text,
        the optimal solution is at the very beginning of the string
        """
        
        k = 8
        text = "AGCAGCTTTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATCTGAACTGGTTACCTGCCGTGAGTAAAT"
        profile = [
            [0.7, 0.2, 0.1, 0.5, 0.4, 0.3, 0.2, 0.1],
            [0.2, 0.2, 0.5, 0.4, 0.2, 0.3, 0.1, 0.6],
            [0.1, 0.3, 0.2, 0.1, 0.2, 0.1, 0.4, 0.2],
            [0.0, 0.3, 0.2, 0.0, 0.2, 0.3, 0.3, 0.1]
        ]
        
        correct_output = "AGCAGCTT"
        result = BA2C.find_profile_probable_kmer(text, k , profile)
        
        assert correct_output == result

    def test_off_by_one_end(self):
        """This dataset checks for off-by-one errors at the end of Text,
        the optimal solution is at the very end of the string
        """
        
        k = 12
        text = "TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTGCGCTTTGTAAGCAGAGTTTA"
        profile = [
            [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.1, 0.2, 0.3, 0.4, 0.5],
            [0.3, 0.2, 0.1, 0.1, 0.2, 0.1, 0.1, 0.4, 0.3, 0.2, 0.2, 0.1],
            [0.2, 0.1, 0.4, 0.3, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.2, 0.1],
            [0.3, 0.4, 0.1, 0.1, 0.1, 0.1, 0.0, 0.2, 0.4, 0.4, 0.2, 0.3]
        ]
        
        correct_output = "AAGCAGAGTTTA"
        result = BA2C.find_profile_probable_kmer(text, k , profile)
        
        assert correct_output == result
    
    def test_general_case_large(self):
        """general case test with a bigger dataset"""
        
        k = 6
        text = "TGCCCGAGCTATCTTATGCGCATCGCATGCGGACCCTTCCCTAGGCTTGTCGCAAGCCATTATCCTGGGCGCTAGTTGCGCGAGTATTGTCAGACCTGATGACGCTGTAAGCTAGCGTGTTCAGCGGCGCGCAATGAGCGGTTTAGATCACAGAATCCTTTGGCGTATTCCTATCCGTTACATCACCTTCCTCACCCCTA"
            
        profile = [
            [0.364, 0.333, 0.303, 0.212, 0.121, 0.242],
            [0.182, 0.182, 0.212, 0.303, 0.182, 0.303],
            [0.121, 0.303, 0.182, 0.273, 0.333, 0.303],
            [0.333, 0.182, 0.303, 0.212, 0.364, 0.152]
        ]
        
        correct_output = "TGTCGC"
        result = BA2C.find_profile_probable_kmer(text, k , profile)
        
        assert correct_output == result