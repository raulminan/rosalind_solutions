from exercises import BA1J

class Test:
    def test_freq_words_mismatches_reverse(self):
        text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
        k = 4
        d = 1
        correct_output = ["ATGT", "ACAT"]
        result = BA1J.frequent_words_with_mismatches_complement(text, k, d)
        assert set(correct_output) == set(result)