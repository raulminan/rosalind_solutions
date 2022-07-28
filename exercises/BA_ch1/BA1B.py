import os
from exercises import BA1K, BA1M

def frequent_words(text, k) -> str:
    """Find the most frequent k-mer in a string

    Parameters
    ----------
    text : str
    k : int
        

    Returns
    -------
    str
        most frequent k-mer(s)
    """
    kmers = {} # create a dict to store all kmers and their count
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i + k]
        if pattern not in kmers:
            kmers[pattern] = 0 # if kmer not seen yet, add it to the dict
        kmers[pattern] += 1
    
    frequent_kmers = []
    max_count = max(kmers.values())
    for k, v in kmers.items():
        if v == max_count:
            frequent_kmers.append(k)
    
    frequent_kmers = sorted(frequent_kmers)
    return(" ".join([str(x) for x in frequent_kmers]))

def faster_frequent_words(text: str, k: int, t: int = 0) -> str:
    """Finds all most frequent k-mers by by finding all k-mers corresponding
    to the maximum element(s) in the frequency array

    Parameters
    ----------
    text : str
        DNA string where k-mers will be found
    k : int
        length of the k-mers
    t : int, optional
        minimun times a k-mer needs to appear for it to be returned, default = 0
    Returns
    -------
    str
        str with the most frequent kmers
    """
    frequent_patterns = set()
    frequency_array = BA1K.computing_frequencies(text, k, output_str=False)
         
    max_count = max(frequency_array)
    for i in range(0, 4**k):
        if frequency_array[i] == max_count and frequency_array[i] >= t:
            pattern = BA1M.number_to_pattern(i, k)
            frequent_patterns.add(pattern)
    frequent_patterns = sorted(frequent_patterns)
    return " ".join(frequent_patterns)

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "rosalind_ba1b.txt")
    with open(filename) as f:
        text = f.readline().strip()
        k = int(f.readline().strip())
    
    frequent = frequent_words(text, k)
    faster_frequent = faster_frequent_words(text, k) 
    print(frequent)
    print(faster_frequent)