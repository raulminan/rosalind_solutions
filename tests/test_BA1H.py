import pytest
from exercises import BA1H

class Test:
    def test_BA1H(self):
        pattern = "ATTCTGGA"
        text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"
        d = 3
        output = "6 7 26 27 78"
        
        assert output == BA1H.approx_pattern_matching(pattern, text, d)