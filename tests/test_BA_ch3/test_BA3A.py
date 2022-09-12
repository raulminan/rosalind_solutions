from exercises.BA_ch3 import BA3A

class Tests:
    def test_string_composition(self):
        """general case for string composition
        """
        k = 5
        text = "CAATCCAAC"
        correct_output = {
            "AATCC",
            "ATCCA",
            "CAATC",
            "CCAAC",
            "TCCAA"
        }
        
        result = BA3A.string_composition(text, k)
        assert result == correct_output