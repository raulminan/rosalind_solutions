from exercises.BA_ch2 import BA2D


# TODO fix tests: Some fail even when the answer is correct

class Tests():
    def test_build_profile(self):
        """General case test for build_profile
        """
        dna = ["TCGGGGGTTTTT",
               "CCGGTGACTTAC",
               "ACGGGGATTTTC",
               "TTGGGGACTTTT",
               "AAGGGGACTTCC",
               "TTGGGGACTTCC",
               "TCGGGGATTCAT",
               "TCGGGGATTCCT",
               "TAGGGGAACTAC",
               "TCGGGTATAACC"]
        t = 10
        k = 12
        
        correct_output = [
            [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
            [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
            [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
        ]
        result = BA2D.build_profile(dna, k, t)
        
        assert correct_output == result
         
    def test_find_consensus(self):
        """General case for the consesus function
        """
        motifs = ["TCGGGGGTTTTT",
            "CCGGTGACTTAC",
            "ACGGGGATTTTC",
            "TTGGGGACTTTT",
            "AAGGGGACTTCC",
            "TTGGGGACTTCC",
            "TCGGGGATTCAT",
            "TCGGGGATTCCT",
            "TAGGGGAACTAC",
            "TCGGGTATAACC"]
        
        correct_output = "TCGGGGATTTCC"
        result = BA2D.find_consensus(motifs)
        
        assert correct_output == result
    
    def test_score_motifs(self):
        """General test case for this function"""
        
        motifs = ["TCGGGGGTTTTT",
            "CCGGTGACTTAC",
            "ACGGGGATTTTC",
            "TTGGGGACTTTT",
            "AAGGGGACTTCC",
            "TTGGGGACTTCC",
            "TCGGGGATTCAT",
            "TCGGGGATTCCT",
            "TAGGGGAACTAC",
            "TCGGGTATAACC"]
        
        correct_output = 30
        result = BA2D.score_motifs(motifs)
        
        assert correct_output == result    
    
    
    def test_greedy_motif_search(self):
        """General case for this function"""
        dna = ["GGCGTTCAGGCA",
            "AAGAATCAGTCA",
            "CAAGGAGTTCGC",
            "CACGTCAATCAC",
            "CAATAATATTCG"]
        k = 3
        t = 5
        correct_output = ["CAG", "CAG", "CAA", "CAA", "CAA"]
        result = BA2D.greedy_motif_search(dna, k, t)
        
        assert correct_output == result
    
    def test_greedy_motif_search_sample(self):
        """Tesdfg
        """
        k = 3
        t = 5
        dna = ["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"]
        output = ["CAG", "CAG", "CAA", "CAA", "CAA"]
        result = BA2D.greedy_motif_search(dna, k, t)
        
        assert output == result
        
        
    def test_greedy_picks_first(self):
        """This dataset checks that the code always picks the 1st-occurring profile
        most probable k-mer
        """
        k = 3
        t = 4
        dna = ["GCCCAA", "GGCCTG", "AACCTA", "TTCCTT"]
        output = ["GCC", "GCC", "AAC", "TTC"]
        result = BA2D.greedy_motif_search(dna, k, t)
        
        assert output == result
        
    def test_greedy_off_by_one_begin(self):
        """This dataset checks if the code has a off by one error at the beginning of 
        each sequence of dna
        """
        k = 5
        t = 8
        dna = [
            "GAGGCGCACATCATTATCGATAACGATTCGCCGCATTGCC",
            "TCATCGAATCCGATAACTGACACCTGCTCTGGCACCGCTC",
            "TCGGCGGTATAGCCAGAAAGCGTAGTGCCAATAATTTCCT",
            "GAGTCGTGGTGAAGTGTGGGTTATGGGGAAAGGCAGACTG",
            "GACGGCAACTACGGTTACAACGCAGCAACCGAAGAATATT",
            "TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT",
            "AAGCGGCCAACGTAGGCGCGGCTTGGCATCTCGGTGTGTG",
            "AATTGAAAGGCGCATCTTACTCTTTTCGCTTTCAAAAAAA"
        ]
        output = ["GAGGC", "TCATC", "TCGGC", "GAGTC", "GCAGC", "GCGGC", "GCGGC", "GCATC"]
        result = BA2D.greedy_motif_search(dna, k, t)
        
        assert output == result
        
    def test_greedy_off_by_one_end(self):
        """This dataset checks if the code has a off by one error at the end of 
        each sequence of dna
        """
        k = 6
        t = 5
        dna = [
            "GCAGGTTAATACCGCGGATCAGCTGAGAAACCGGAATGTGCGT",
            "CCTGCATGCCCGGTTTGAGGAACATCAGCGAAGAACTGTGCGT",
            "GCGCCAGTAACCCGTGCCAGTCAGGTTAATGGCAGTAACATTT",
            "AACCCGTGCCAGTCAGGTTAATGGCAGTAACATTTATGCCTTC",
            "ATGCCTTCCGCGCCAATTGTTCGTATCGTCGCCACTTCGAGTG"
        ]
        output = ["GTGCGT", "GTGCGT", "GCGCCA", "GTGCCA", "GCGCCA"]
        result = BA2D.greedy_motif_search(dna, k, t)
        
        assert output == result
        
    def test_greedy_tie_breaker(self):
        """This test dataset checks if your code is correctly breaking ties when calling 
        Proﬁle-most Probable k-mer. Speciﬁcally, it makes sure that, when you call 
        Proﬁle-most Probable k-mer, in the event of a tie, you choose the ﬁrst-occurring 
        k-mer.
        """
        k = 5
        t = 8
        dna = [
            "GACCTACGGTTACAACGCAGCAACCGAAGAATATTGGCAA",
            "TCATTATCGATAACGATTCGCCGGAGGCCATTGCCGCACA",
            "GGAGTCTGGTGAAGTGTGGGTTATGGGGCAGACTGGGAAA",
            "GAATCCGATAACTGACACCTGCTCTGGCACCGCTCTCATC",
            "AAGCGCGTAGGCGCGGCTTGGCATCTCGGTGTGTGGCCAA",
            "AATTGAAAGGCGCATCTTACTCTTTTCGCTTAAAATCAAA",
            "GGTATAGCCAGAAAGCGTAGTTAATTTCGGCTCCTGCCAA",
            "TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT"
        ]
        output = ["GCAGC", "TCATT", "GGAGT", "TCATC", "GCATC", "GCATC", "GGTAT", "GCAAC"]
        result = BA2D.greedy_motif_search(dna, k, t)
        
        assert output == result