from exercises.BA_ch2 import BA2H

class Tests:
    def test_d_pattern_and_string(self):
        pattern = "AAA"
        dna = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]
        correct_output = 5
        my_result = BA2H.d_pattern_and_strings(pattern, dna)
        
        assert correct_output == my_result