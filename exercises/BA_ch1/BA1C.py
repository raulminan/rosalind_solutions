import os

def reverse_complement(pattern) -> str:
    """Returns the reverse complement of a DNA string

    Parameters
    ----------
    pattern : str
        DNA string

    Returns
    -------
    str
        reverse complement of pattern
    """
    bases = {
        "A": "T",
        "C": "G",
        "G": "C",
        "T": "A",
    }
    
    complement = ""
    
    for i in pattern:
        complement += bases[i]
    
    reverse_complement_ = complement[::-1]
    return reverse_complement_

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "rosalind_ba1c.txt")
    with open(filename) as f:
        pattern = f.readline().strip()
    
    print(reverse_complement(pattern))