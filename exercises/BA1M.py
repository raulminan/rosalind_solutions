import os


def number_to_symbol(index: int) -> str:
    numb_to_symb = {
        0: "A",
        1: "C",
        2: "G",
        3: "T"
    }
    return numb_to_symb[index]

def quotient(index: int, k: int) -> int:
    return index // k

def remainder(index: int, k: int) -> int:
    return index % k

def number_to_pattern(index: int, k: int) -> str:
    """Compute a DNA string (DNA pattern) given an integer that represents its 
    position when all patterns of length k are ordered lexicographically

    Parameters
    ----------
    index : int
        position that the pattern would occupy when ordered lexicographically
    k : int
        length of the pattern

    Returns
    -------
    str
        DNA pattern
    """
    if k == 1:
        return number_to_symbol(index)
    
    prefix_index = quotient(index, 4)
    remainder_ = remainder(index, 4)
    symbol = number_to_symbol(remainder_)
    prefix_pattern = number_to_pattern(prefix_index, k-1)
    
    return prefix_pattern + symbol


if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "rosalind_ba1m.txt")
    with open(filename) as f:
        index = int(f.readline().strip())
        k = int(f.readline().strip())
        
    print(number_to_pattern(index, k))