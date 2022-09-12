from exercises import utils
from exercises.BA_ch2 import BA2C, BA2D, BA2E

import random

def select_kmers(dna, k):
    random_motifs = []
    for string in dna:
        idx = random.randrange(0, len(string) - k + 1)
        motif = string[idx:idx+k]
        random_motifs.append(motif)
    return random_motifs
        
def randomized_motif_search(dna: list, k: int, t: int) -> list:
    """A randomized approac to findind the best motif in a list if dna strings

    Parameters
    ----------
    dna : list
        list of dna strings
    k : int
        length of each string
    t : int
        number of strings

    Returns
    -------
    list
        best motifs
    """
    motifs = select_kmers(dna, k)
    best_motifs = motifs
    while True:
        profile = BA2E.build_profile_pseudocounts(motifs, k , t)
        motifs = [BA2C.find_profile_probable_kmer(string, k, profile) for string in dna]
        if BA2D.score_motifs(motifs) < BA2D.score_motifs(best_motifs):
            best_motifs = motifs
        else: 
            return best_motifs

if __name__ == "__main__":
    filename = utils.load_file("ba2f")
    with open(filename) as f:
        k, t = list(map(int, f.readline().strip().split()))
        dna = f.read().splitlines()
    
    best_motifs = randomized_motif_search(dna, k, t)
    for _ in range(999):
        motifs = randomized_motif_search(dna, k, t)
        if BA2D.score_motifs(motifs) < BA2D.score_motifs(best_motifs):
            best_motifs = motifs
        
    print("\n".join(best_motifs))    