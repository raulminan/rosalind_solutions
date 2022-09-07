from exercises import utils
from exercises.BA_ch1 import BA1M
from exercises.BA_ch2 import BA2H

def median_string(dna: list, k: int) -> str:
    """Given a k-mer 'pattern' and a longer string 'text', we use d(pattern, text)
    to denote the minimum Hamming Distance between 'pattern' and any k-mer in 'text'
    
    d (pattern, text) = -----------min------------- hamming_distance(pattern, pattern')
                        all kmers pattern'in text

    Given a k-mer 'pattern' and a set of strings dna = {dna_1, ... dna_t}, we define
    d(pattern, dna) as the sum of the distinces between pattern and all strings in dna
    
    d (pattern, dna) = \sum_{i=1}^{t} d(pattern, dna_i) 
    
    This function finds a k-mer pattern that minimizes d(pattern, dna) over all k-mers
    pattern.
    
    Parameters
    ----------
    dna : list
        collection of dna strings
    k : int
        length of k-mer

    Returns
    -------
    str
        A k-mer that minimizes d(pattern, dna) over all k-mers pattern. This is the 
        median string
    """
    distance = float("inf")
    for i in range(4**k):
        pattern = BA1M.number_to_pattern(i, k)
        if distance > BA2H.d_pattern_and_strings(pattern, dna):
            distance = BA2H.d_pattern_and_strings(pattern, dna)
            median_string = pattern
    
    # ===========================================================
    # # use only kmers appearing in dna
    # long_dna = "".join(dna) ==> this wont work because dna strings must remain 
    #                             separate. Instead, loop trough each dna string
    #                             and get all kmers appearing there #TODO
    
    # for i in range(0, long_dna - k + 1):
    #     pattern = long_dna[i:i+k]
    #     if distance > BA2H.d_pattern_and_strings(pattern, dna):
    #         distance = BA2H.d_pattern_and_strings(pattern, dna)
    #         median_string = pattern
    # ===========================================================
    
    return median_string

if __name__ == "__main__":
    filename = utils.load_file("ba2b")
    with open(filename) as f:
        k = int(f.readline().strip())
        dna = f.read().splitlines()
        
        median_string_ = median_string(dna, k)
        print(median_string_)