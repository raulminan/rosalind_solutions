from exercises.BA_ch3 import BA3B

class Tests:
    def test_reconstruct_string(self):
        kmers = [
            "ACCGA",
            "CCGAA",
            "CGAAG",
            "GAAGC",
            "AAGCT"
        ]
        correct_output = "ACCGAAGCT"
        result = BA3B.string_reconstruct(kmers)
        
        assert correct_output == result