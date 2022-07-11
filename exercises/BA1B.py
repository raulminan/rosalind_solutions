import os

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
    return(frequent_kmers)

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "rosalind_ba1b.txt")
    with open(filename) as f:
        text = f.readline().strip()
        k = int(f.readline().strip())
    
    frequent = frequent_words(text, k)
    for i in frequent:
        print(i)