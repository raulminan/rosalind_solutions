from exercises.BA_ch2 import BA2D, BA2F

# TODO again, tests fail but the answer is correct ¯\_(ツ)_/¯ 

class Tests():
    def test_random_motif_search(self):
        """General case for ramdomized motif search
        """
        k = 8
        t = 5
        motifs = [
            "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
            "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
            "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
            "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
            "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
        ]
        output = [
            "TCTCGGGG",
            "CCAAGGTG",
            "TACAGGCG",
            "TTCAGGTG",
            "TCCACGTG"
        ]
        
        
        best_motifs = BA2F.randomized_motif_search(motifs, k, t)
        for _ in range(1000):
            motifs = BA2F.randomized_motif_search(motifs, k, t)
            if BA2D.score_motifs(motifs) < BA2D.score_motifs(best_motifs):
                best_motifs = motifs
    
        assert output == best_motifs
