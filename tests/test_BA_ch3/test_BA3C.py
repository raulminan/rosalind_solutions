from exercises.BA_ch3 import BA3C

class Tests:
    def test_graph_overlap(self):
        patterns = [
        "ATGCG",
        "GCATG",
        "CATGC",
        "AGGCA",
        "GGCAT"
        ]
        correct_output = [
            "AGGCA -> GGCAT",
            "CATGC -> ATGCG",
            "GCATG -> CATGC",
            "GGCAT -> GCATG"
        ]
        result = BA3C.overlap_graph(patterns)
        
        assert correct_output == result
        