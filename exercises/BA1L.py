import os

def last_symbol(pattern: str) -> str:
    """Returns the last letter of a string"""
    return pattern[-1]

def prefix(pattern: str) -> str:
    """Returns all but the last letter of a string"""
    return pattern[:-1]

def symbol_to_number(symbol: str) -> int:
    """Converts a DNA base into a int based on lexicographic order"""
    values = {
        "A": 0,
        "C": 1,
        "G": 2,
        "T": 3
    }
    return values[symbol.upper()]

def pattern_to_number(pattern: str) -> int:
    """Given a DNA string, convert it to a number corresponding to
    its position when ordered lexicographically

    Parameters
    ----------
    pattern : str
        DNA string to convert to a number

    Returns
    -------
    int
    
    """
    if not pattern:
        return 0
    
    prefix_ = prefix(pattern)
    symbol = last_symbol(pattern)
    return 4 * pattern_to_number(prefix_) + symbol_to_number(symbol)


if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "rosalind_ba1l.txt")
    with open(filename) as f:
        pattern = f.readline().strip()
        
    print(pattern_to_number(pattern))
    
  
    