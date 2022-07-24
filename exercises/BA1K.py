import os
import numpy as np
from exercises import BA1L

def computing_frequencies(text: str, k: int) -> str:
    """Generate a frequency array of a string as an array of length
    4**k, where the i-ith element of the array holds the number of times
    that the i-th k-mer (in lexicographic order) appears in text

    Parameters
    ----------
    text : str
    k : int

    Returns
    -------
    str
        frequency array
    """
    frequency_array = [0 for _ in range(0, 4**k)]
    for i in range(0, len(text)-k+1):
        pattern = text[i:i+k]
        j = BA1L.pattern_to_number(pattern)
        frequency_array[j] = frequency_array[j] + 1
    
    return " ".join([str(x) for x in frequency_array])

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "rosalind_ba1k.txt")
    with open(filename) as f:
        text = f.readline().strip()
        k = int(f.readline().strip())
        
    print(computing_frequencies(text, k))