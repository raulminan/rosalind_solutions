from exercises import utils

def string_composition(text: str, k: int, sorted=False) -> set:
    """Generates the k-mer composition of a string, or the collection of all 
    k-mer substrings of a string

    Parameters
    ----------
    text : str
    k : int
    sorted: bool, optional
        Parameter to control wether the string composition is sorted alphabetically, 
        if True, by default False

    Returns
    -------
    dict
        collection of k-mers
    """
    composition = set()
    for i in range(0, len(text) - k + 1):
        kmer = text[i:i+k]
        composition.add(kmer)
        
    if sorted:
        composition = list(composition).sort()
    
    return composition

if __name__ == "__main__":
    filename = utils.load_file("ba3a")
    with open(filename) as f:
        k = int(f.readline().strip())
        text = f.readline().strip()
    
    comp = string_composition(text, k)
    print("\n".join(comp))
