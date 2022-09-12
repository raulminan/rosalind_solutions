from exercises import utils

def string_reconstruct(kmers: list) -> str:
    """Reconstruct a string from its genome path

    Parameters
    ----------
    kmers : list
        A sequence of k-mers Patter1, ..., Pattern_n such that the last k-1 symbols
        of Pattern_i are equal to the first k-1 symbols of Pattern_{i+1} for 1 <= i <= n

    Returns
    -------
    str
        string if length k + n - 1 such that the i-th k-mer in text is equal to 
        pattern_i (for 1 <= i <= n)
    """
    string = kmers[0]
    for i in range(1, len(kmers)):
        kmer = kmers[i]
        string += kmer[-1]
    return string

if __name__ == "__main__":
    filename = utils.load_file("ba3b")
    with open(filename) as f:
        kmers = f.read().splitlines()
    
    print(string_reconstruct(kmers))