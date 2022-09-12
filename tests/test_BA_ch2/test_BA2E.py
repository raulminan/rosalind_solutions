from exercises.BA_ch2 import BA2E

class Tests():
    def test_greedy_pseudocounts(self):
        """General case for greedy_motif_search with pseudocounts
        """
        k = 3
        t = 5
        motifs = [
            "GGCGTTCAGGCA",
            "AAGAATCAGTCA",
            "CAAGGAGTTCGC",
            "CACGTCAATCAC",
            "CAATAATATTCG"
        ]
        output = ["TTC", "ATC", "TTC", "ATC", "TTC"]
        result = BA2E.greedy_motif_search_pseudocounts(motifs, k, t)
        
        assert output == result

