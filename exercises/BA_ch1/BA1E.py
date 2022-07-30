import os
import re
from exercises.BA_ch1 import BA1B, BA1M, BA1K, BA1L

# TODO debug 
def find_clumps_frequent_words(genome: str, k: int, L: int, t: int) -> str:
    """Computes every k-mer that forms a clump in the genome
    
    We define a k-mer as a "clump" if it appears many times within a short interval 
    of the genome, formally: 
    
    Given integers L and t, a k-mer "Pattern" forms an (L, t)-clump inside a 
    longer string "Genome" if there is an interval of Genome of length L in which
    tgis k-mer appears at least t times

    Parameters
    ----------
    genome : str
        Genome in which the clumps are going to be found
    k : int
        length of the clumps
    L : int
        interval of genomes in which the clumps appears
    t : int
        number of times a given k-mer needs to appear within an interval of genome
        for it to be considered a clump

    Returns
    -------
    str
        all distinct k-mers forming (L, t)-clumps in Genome
        
    Example
    -------
    "TGCA" forms a (25,3)-clump in the following genome:
    
    gatcagcataagggtcccTGCAaTGCAtgacaagccTGCAgttgttttac
    """ 
    # TODO debug this function
    global_patterns = []
    for i in range(0, len(genome) - L + 1):
        window = genome[i:i+L]
        frequent_patterns = BA1B.faster_frequent_words(window, k, t).split(" ")
        global_patterns.extend(frequent_patterns)
    
    return " ".join(global_patterns)

# TODO debug
def clump_finding(genome: str, k: int, L: int, t: int) -> str:
    """Computes every k-mer that forms a clump in the genome
    
    We define a k-mer as a "clump" if it appears many times within a short interval 
    of the genome, formally: 
    
    Given integers L and t, a k-mer "Pattern" forms an (L, t)-clump inside a 
    longer string "Genome" if there is an interval of Genome of length L in which
    tgis k-mer appears at least t times

    Parameters
    ----------
    genome : str
        Genome in which the clumps are going to be found
    k : int
        length of the clumps
    L : int
        interval of genomes in which the clumps appears
    t : int
        number of times a given k-mer needs to appear within an interval of genome
        for it to be considered a clump

    Returns
    -------
    str
        all distinct k-mers forming (L, t)-clumps in Genome
        
    Example
    -------
    "TGCA" forms a (25,3)-clump in the following genome:
    
    gatcagcataagggtcccTGCAaTGCAtgacaagccTGCAgttgttttac
    """
    frequent_patterns = []
    clump = [0] * 4**k
    
    for i in range(0, len(genome) - L + 1):
        window = genome[i:i+L]
        frequency_array = BA1K.computing_frequencies(window, k, output_str=False)
        for j in range (0, 4**k):
            if frequency_array[j] >= t:
                clump[j] = 1
                
    for i in range(0, 4**k):
        if clump[i] == 1:
            pattern = BA1M.number_to_pattern(i, k)
            frequent_patterns.append(pattern)
    return " ".join(frequent_patterns)

def better_clump_finding(genome: str, k: int, t: int, L: int):
    """A faster version of clump_finding:
    
    Computes every k-mer that forms a clump in the genome
    
    We define a k-mer as a "clump" if it appears many times within a short interval 
    of the genome, formally: 
    
    Given integers L and t, a k-mer "Pattern" forms an (L, t)-clump inside a 
    longer string "Genome" if there is an interval of Genome of length L in which
    tgis k-mer appears at least t times

    Parameters
    ----------
    genome : str
        Genome in which the clumps are going to be found
    k : int
        length of the clumps
    L : int
        interval of genomes in which the clumps appears
    t : int
        number of times a given k-mer needs to appear within an interval of genome
        for it to be considered a clump

    Returns
    -------
    str
        all distinct k-mers forming (L, t)-clumps in Genome
        
    Example
    -------
    "TGCA" forms a (25,3)-clump in the following genome:
    
    gatcagcataagggtcccTGCAaTGCAtgacaagccTGCAgttgttttac
    """
    frequent_patterns = set()
    clump = [0] * 4**k
    text = genome[0:L]
    frequency_array = BA1K.computing_frequencies(text, k, output_str=False)
    for i in range(0, 4**k):
        if frequency_array[i] >= t:
            clump[i] = 1
  
    for i in range(1, len(genome) - L + 1):
        first_pattern = genome[i-1:i-1+k]
        index = BA1L.pattern_to_number(first_pattern)
        frequency_array[index] -= 1
        last_pattern = genome[i+L-k:i+L]
        index = BA1L.pattern_to_number(last_pattern)
        frequency_array[index] += 1
        if frequency_array[index] >= t:
            clump[index] = 1
    
    for i in range(0, 4**k):
        if clump[i] == 1:
            pattern = BA1M.number_to_pattern(i, k)
            frequent_patterns.add(pattern)
    
    return frequent_patterns


if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "rosalind_ba1e.txt")
    with open(filename) as f:
        genome = f.readline().strip()
        k, L, t = list(map(int, f.readline().strip().split(" ")))
        
    clumps = " ".join(better_clump_finding(genome, k, t, L))
    print(clumps)