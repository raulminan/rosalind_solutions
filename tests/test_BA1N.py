from exercises import BA1N

class Tests:
    def test_neighbors(self):
        """Tests general case for neighbors"""
        pattern = "ACG"
        d = 1
        result = [
            "CCG",
            "TCG",
            "GCG",
            "AAG",
            "ATG",
            "AGG",
            "ACA",
            "ACC",
            "ACT",
            "ACG"
        ]
        assert set(result) == set(BA1N.neighbors(pattern, d))
