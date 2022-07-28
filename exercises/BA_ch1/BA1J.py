from exercises import utils, BA1C, BA1I, BA1L, BA1M, BA1N

def frequent_words_with_mismatches_complement(text: str, k: int, d: int) -> list:
    """Finds the most frequent k-mers (with mismatches and reverse complements)
    in a string

    Parameters
    ----------
    text : str
        DNA string
    k : int
        length of kmer
    d : int
        max amount of mismatches

    Returns
    -------
    list
        list with the most frequent k-mers
    """
    frequent_patterns = []
    close = [0] * 4**k
    frequency_array = [0] * 4**k
    
    for i in range(0, len(text) - k + 1):
        neigborhood = BA1N.neighbors(text[i:i+k], d)
        for pattern in neigborhood:
            index = BA1L.pattern_to_number(pattern)
            close[index] = 1
    
    for i in range(4**k):
        if close[i] == 1:
            pattern = BA1M.number_to_pattern(i, k)
            reverse = BA1C.reverse_complement(pattern)
            count_pattern = BA1I.approximate_pattern_count(text, pattern, d)
            count_reverse = BA1I.approximate_pattern_count(text, reverse, d)
            frequency_array[i] = count_pattern + count_reverse
    
    max_count = max(frequency_array)
    for i in range(4**k):
        if frequency_array[i] == max_count:
            pattern = BA1M.number_to_pattern(i, k)
            frequent_patterns.append(pattern)
    
    return frequent_patterns

if __name__ == "__main__":
    filename = utils.load_file("ba1j")
    with open(filename) as f:
        text = f.readline().strip()
        k, d = list(map(int, f.readline().strip().split()))
    
    frequent_patterns = frequent_words_with_mismatches_complement(text, k, d)
    print(" ".join(frequent_patterns))