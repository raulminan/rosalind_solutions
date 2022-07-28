import os 

def find_occurences(pattern: str, genome:str) -> str:
    """Find all occurences of a pattern in a genome

    Parameters
    ----------
    pattern : str
    genome : str

    Returns
    -------
    str
        str with all starting positions in genome where pattern appears as substring
    """
    positions = []
    
    for i in range(0, len(genome)-len(pattern)+1):
        if genome[i:i+len(pattern)] == pattern:
            positions.append(i)
            
    return " ".join([str(x) for x in positions])



if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "rosalind_ba1d.txt")
    with open(filename) as f:
        pattern = f.readline().strip()
        genome = f.readline().strip()
        
    print(find_occurences(pattern, genome))