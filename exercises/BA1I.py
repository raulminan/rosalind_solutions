from exercises import utils, BA1G, BA1L, BA1M, BA1N


def approximate_pattern_count(text: str, pattern: str, d: int) -> int:
    """Counts the number of approximate matches for a given maximum hamming distance

    Parameters
    ----------
    text : str
        string to find the matches in 
    pattern : str
        string to match in text
    d : int
        max hamming distance

    Returns
    -------
    int
        number of approximate matches
    """
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        substring = text[i:i+len(pattern)]
        if BA1G.hamming_distance(substring, pattern) <= d:
            count += 1
    
    return count

def frequent_words_with_mismatches(text: str, k: int, d: int) -> str:
    """Finds the most frequent k-mer in text with at most d mismatches

    Parameters
    ----------
    text : str
    k : int
        k-mer length
    d : int
        max number of mismatches for each match

    Returns
    -------
    str
        string with all the most frequent k-mers with up to d mismatches
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
            frequency_array[i] = approximate_pattern_count(text, pattern, d)
    
    max_count = max(frequency_array)
    for i in range(4**k):
        if frequency_array[i] == max_count:
            pattern = BA1M.number_to_pattern(i, k)
            frequent_patterns.append(pattern)
    
    return frequent_patterns

if __name__ == "__main__":
    filename = utils.load_file("ba1i")
    with open(filename) as f:
        text = f.readline().strip()
        k, d = list(map(int, (f.readline().strip().split(" "))))
    
    frequent_patterns = frequent_words_with_mismatches(text, k, d)
    print(" ".join(frequent_patterns))
        
       