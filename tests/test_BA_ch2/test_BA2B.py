from exercises.BA_ch2 import BA2B

class Tests:
    def test_median_string(self):
        k = 3
        dna = [
            "AAATTGACGCAT",
            "GACGACCACGTT",
            "CGTCAGCGCCTG",
            "GCTGAGCACCGG",
            "AGTACGGGACAG"
        ]
        correct_output = "GAC"
        my_result = BA2B.median_string(dna, k)
        
        assert correct_output == my_result