from exercises import utils
from operator import mul
from functools import reduce

def find_profile_probable_kmer(text: str, k:int, profile: list) -> str:
    """Find a profile-most probable k-mer in a string

    Parameters
    ----------
    text : str
        string of dna
    k : int
        length of k-mer
    profile : list
        4*k matrix with the profile. List of 4 lists, where each list is the
        probability of finding the nucleotide A, C, G and T, respectively.

    Returns
    -------
    str
        a profile-most probable k-mer in text
    """
    most_probable = ""
    probability = float("-inf")
    nucleotide_probas = {
        "A": profile[0],
        "C": profile[1],
        "G": profile[2],
        "T": profile[3]
    }
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i+k]
        p_list = []
        for j in range(0, len(pattern)):
            nucleotide = pattern[j]
            p = nucleotide_probas[nucleotide][j]
            p_list.append(p)
        pattern_prob = reduce(mul, p_list, 1)
        if pattern_prob > probability:
            probability = pattern_prob
            most_probable = pattern
            
    return most_probable

def format_profile(profile: list):
    """small helper function to format a profile matrix performing the following
    transformation t0 -> t1:
    
    t0 = ["x x x x", "x x x x", "x x x x", "x x x x", "x x x x"]
    t1 = [[x, x, x, x], [x, x, x, x], [x, x, x, x], [x, x, x, x]]
    
    where each x is a float

    Parameters
    ----------
    profile : list
        profile matrix in the format represented in t0
    """
    profile = [i.split(" ") for i in profile]
    profile = [[float(j) for j in i] for i in profile]
    
    return profile

   
if __name__ == "__main__":
    filename = utils.load_file("ba2c")
    with open(filename) as f:
        text = f.readline().strip()
        k = int(f.readline().strip())
        profile = f.read().splitlines()
        profile = format_profile(profile)
 
    kmer = find_profile_probable_kmer(text, k, profile)
    print(kmer)