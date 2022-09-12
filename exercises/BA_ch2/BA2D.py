from exercises import utils
from exercises.BA_ch1 import BA1G
from exercises.BA_ch2 import BA2C

def build_profile(dna: list, k:int, t: int) -> list:
    """Builds the profile for a motif matrix

    Parameters
    ----------
    dna : list
        list of dna strings
    k: int
        length of each dna string
    t : int
        number of dna strings

    Returns
    -------
    list
        list of t lists, where each list t_i contains the profile for dna string dna_i
    """
    A, C, G, T = [], [], [], []
    for j in range(k):
        countA, countC, countG, countT = 0, 0, 0, 0
        for motif in dna:
            if motif[j] == "A":
                countA += 1
            elif motif[j] == "C":
                countC += 1
            elif motif[j] == "G":
                countG += 1
            elif motif[j] == "T":
                countT += 1
        A.append(countA)
        C.append(countC)
        G.append(countG)
        T.append(countT)
    
    count = [A, C, G, T]
    profile = [[j/len(dna) for j in i] for i in count]
    # ^ j/len(dna) or t ? t doesn't make sense but gets the answer right
    return profile

def find_consensus(motifs: list) -> str:
    """Finds the consensus motif in a matrix of motifs

    Parameters
    ----------
    motifs : list
        list of motifs

    Returns
    -------
    str
        consensus motif
    """
    consensus = ""
    k = len(motifs[0])
    t = len(motifs)
    
    for i in range(k):
        count_a, count_c, count_g, count_t = 0, 0, 0, 0
        for motif in motifs:
            if motif[i] == "A":
                count_a += 1
            elif motif[i] == "C":
                count_c += 1
            elif motif[i] == "G":
                count_g += 1
            elif motif[i] == "T":
                count_t += 1
                
        if count_a >= max(count_c, count_g, count_t):
            consensus += "A"
        elif count_c >= max(count_a, count_g, count_t):
            consensus += "C"
        elif count_g >= max(count_c, count_a, count_t):
            consensus += "G"
        elif count_t >= max(count_c, count_g, count_a):
            consensus += "T"
            
    return consensus

def score_motifs(motifs: list) -> int:
    """Returns the score of a list of motifs

    Parameters
    ----------
    motifs : list
        list of motifs

    Returns
    -------
    int
        Total number of mismatches between each motif and the consensus motif
    """
    score = 0
    consensus = find_consensus(motifs)
    for motif in motifs:
        score += BA1G.hamming_distance(motif, consensus)
        
    return score
           
def greedy_motif_search(dna: list, k: int, t: int) -> list:
    """A greedy approach to finding the best motif.

    Parameters
    ----------
    dna : list
        list of dna strings
    k : int
        length of k-mer
    t : int
        number of dna strings

    Returns
    -------
    list
        list with the best motifs
    """
    # best_motifs = [dna[i][:k] for i in range(t)] # motif matrix formed by the first k-mers
    #                                              # in each string of dna
    best_score = float("inf")
    best_motifs = []
    for string in dna:
        best_motifs.append(string[:k])
        
    dna_1 = dna[0]
    for i in range(t - k + 1):
        motif_1 = dna_1[i:i+k]
        motifs = [motif_1]
        for j in range(1, t):
            profile = build_profile(motifs, k, t)
            motif_i = BA2C.find_profile_probable_kmer(dna[j], k, profile)
            motifs.append(motif_i)
        if score_motifs(motifs) < best_score:
            best_score = score_motifs(motifs)
            best_motifs = motifs
        
    return best_motifs             

if __name__ == "__main__":
    filename = utils.load_file("ba2d")
    with open(filename) as f:
        k, t = list(map(int, f.readline().strip().split()))
        dna = f.read().splitlines()
        
    motifs = greedy_motif_search(dna, k, t)
    print("\n".join(motifs))