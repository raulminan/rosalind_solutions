from exercises import utils
from exercises.BA_ch1 import BA1H, BA1N

def motif_enumeration(dna: list, k: int, d: int) -> list:
    """Finds all (k, d)-motifs in a collection of strings
    
    A k-mer is a (k, d)-motif if it appears in every string in dna with at most
    d mismatches.

    Parameters
    ----------
    dna : list
        list of dna strings
    k : int
        length of k-mer
    d : int
        max number of mismatches allowed

    Returns
    -------
    list
        all (k, d)-motifs in dna
    """
    patterns = set()
    long_dna = "".join(dna)
    
    for i in range(0, len(long_dna) - k + 1):
        pattern = long_dna[i:i+k] 
        neighbors = BA1N.neighbors(pattern, d) # for each k-mer, generate neighbors at d
        for neighbor in neighbors: # for all neighbors, check if the are in all strings
            count = 0
            for dna_string in dna:
                if BA1H.approx_pattern_matching(neighbor, dna_string, d):
                    count += 1
            if count == len(dna):
                patterns.add(neighbor)
    return patterns

if __name__ == "__main__":
    filename = utils.load_file("ba2a")
    with open(filename) as f:
        k, d = list(map(int, f.readline().strip().split()))
        dna = f.read().splitlines()
        
        motifs = motif_enumeration(dna, k, d)
        print(" ".join(motifs))
        