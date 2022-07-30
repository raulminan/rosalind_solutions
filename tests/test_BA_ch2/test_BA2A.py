from exercises.BA_ch2 import BA2A

class Tests:
    def test_motif_enumeration(self):
        """General case for motif_enumeration"""
        k = 3
        d = 1
        dna = [
            "ATTTGGC",
            "TGCCTTA",
            "CGGTATC",
            "GAAAATT"
        ]
        correct_output = {"ATA", "ATT", "GTT", "TTT"}
        result = BA2A.motif_enumeration(dna, k, d)
        assert correct_output == result