from exercises import utils, BA1G

def suffix(pattern: str) -> str:
    """Returns a string without the first letter"""
    return pattern[1:]

def first_symbol(pattern: str) -> str:
    """Returns the first letter of a string"""
    return pattern[0]

def neighbors(pattern: str, d: int) -> list:
    """Given a DNA string, returns all neighbors within a hamming distance of d

    Parameters
    ----------
    pattern : str
        DNA string
    d : int
        maximum hamming distance

    Returns
    -------
    list
        list with all neighbors within a maximum hamming distance of d
    """
    
    if d == 0:
        return {pattern}
    
    if len(pattern) == 1:
        return {"A", "C", "G", "T"}
    
    neighborhood = set()
    suffix_neighbors = neighbors(suffix(pattern), d)
    for text in suffix_neighbors:
        if BA1G.hamming_distance(suffix(pattern), text) < d:
            for nucleotide in "ATCG":
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(first_symbol(pattern) + text)
    
    return neighborhood

if __name__ == "__main__":
    filename = utils.load_file("ba1n")
    with open(filename) as f:
        pattern = f.readline().strip()
        d = int(f.readline().strip())
    
    print(*neighbors(pattern, d), sep="\n")