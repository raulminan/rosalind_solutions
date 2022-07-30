from exercises import utils
from exercises.BA_ch1 import BA1G

def d_pattern_and_strings(pattern: str, dna: list) -> int:
    """Computes d(pattern, dna), the sum of distances between pattern and each
    string in dna = {dna_1, ... dna_t}
    
    d (pattern, dna) = \\sum_{i=1}^{t} d(pattern, dna) \\ 

    Parameters
    ----------
    pattern : str
        string
    dna : list
        collection of dna strings

    Returns
    -------
    int
        sum of the distances between pattern and each string in dna
    """
    k = len(pattern)
    distance = 0
    for text in dna:
        d = float("inf")
        for i in range(0, len(text) - k + 1):
            pattern_prime = text[i:i+k]
            if d > BA1G.hamming_distance(pattern, pattern_prime):
                d = BA1G.hamming_distance(pattern, pattern_prime)
        distance += d
        
    return distance

if __name__ == "__main__":
    filename = utils.load_file("ba2h")
    with open(filename) as f:
        pattern = f.readline().strip()
        dna = f.readline().strip().split()
    
    d = d_pattern_and_strings(pattern, dna)
    print(d)
    