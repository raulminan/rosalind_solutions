from exercises import BA1I

class Tests:
    def test_frequent_words_with_mismatches(self):
        """test general case
        """
        text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
        k = 4
        d = 1
        correct_output = ["GATG", "ATGC", "ATGT"]
        
        assert set(correct_output) == set(BA1I.frequent_words_with_mismatches(text, k, d))