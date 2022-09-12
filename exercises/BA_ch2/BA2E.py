from exercises import utils
from exercises.BA_ch2 import BA2C, BA2D

# TODO figure out why answer is correct or wrong depending on the dataset

def build_profile_pseudocounts(motifs: list, k:int, t: int) -> list:
    """Builds the profile for a motif matrix using pseudocounts (adding 1 to the count
    of each nucleotide to remove all 0) and Laplace's Rule of Succession
    
    Laplace's Rule of Succession states the following:
    
        If x_1, ... , x_{n+1} are conditionally independent random variables that 
        each can assume the value 0 or 1, then, if we know notthing more about them:
        
        P(X_{n+1} = 1 | X_1 + ... + X_n = s) = (s+1)/(n+2)
    
    This rule can be generalized to any number of possibilities:

        P(A_i | n1, ..., n_m, I_m) = (n_i + 1)/(n + m)
    
    https://en.wikipedia.org/wiki/Rule_of_succession#:~:text=Laplace%20used%20the%20rule%20of,of%20the%20Sun%20rising%20tomorrow.

    Parameters
    ----------
    motifs : list
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
        for motif in motifs:
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
    count_1 = [[j+1 for j in i] for i in count]
    profile = [[j/(len(motifs)+4) for j in i] for i in count_1] # apply generalized Laplace Rule formula
    
    return profile

def greedy_motif_search_pseudocounts(dna: list, k: int, t: int) -> list:
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
    best_score = float("inf")
    best_motifs = []
    for string in dna:
        best_motifs.append(string[:k])
        
    dna_1 = dna[0]
    for i in range(t - k + 1):
        motif_1 = dna_1[i:i+k]
        motifs = [motif_1]
        for j in range(1, t):
            profile = build_profile_pseudocounts(motifs, k, t)
            motif_i = BA2C.find_profile_probable_kmer(dna[j], k, profile)
            motifs.append(motif_i)
        if BA2D.score_motifs(motifs) < best_score:
            best_score = BA2D.score_motifs(motifs)
            best_motifs = motifs
        
    return best_motifs

if __name__ == "__main__":
    filename = utils.load_file("ba2e")
    with open(filename) as f:
        k, t = list(map(int, f.readline().strip().split()))
        dna = f.read().splitlines()
        
    motifs = greedy_motif_search_pseudocounts(dna, k, t)
    print("\n".join(motifs))