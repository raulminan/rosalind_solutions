import pytest
from exercises.BA_ch1 import BA1G

class Tests:
    def test_BA1G(self):
        q, p = "GGGCCGTTGGT", "GGACCGTTGAC"
        output = 3
        
        assert output == BA1G.hamming_distance(p, q)