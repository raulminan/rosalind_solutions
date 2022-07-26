import os
from exercises.utils import load_file

def minimum_skew(genome: str) -> str:
    """Defines the skew of a DNA string, denoted skew(genome) as the difference
    between the total number of occurrences of "G" and "C" in Genome
    
    Let Prefix_i(genome) denote the prefix (i.e., initial subtring) of genome of 
    length i

    Parameters
    ----------
    genome : str
        A DNA string

    Returns
    -------
    str
        all integers i minimizing skew(prefix_i(genome)) over all values of i from
        0 to len(genome) in a string
    
    Example
    --------
    skew(prefix_i("CATGGGCATCGGCCATACGCC")) are:
    0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2
    """
    skew = [0] # first value is always 0, since its the skew for a subtring with
               # length 0
    c_count = 0
    g_count = 0
    for i in range(0, len(genome)):
        if genome[i] == "C":
            c_count += 1
        elif genome[i] == "G":
            g_count += 1
        skew.append(g_count-c_count)
        
    indices = [str(i) for i, x in enumerate(skew) if x == min(skew)]
    return " ".join(indices)

if __name__ == "__main__":
    filename = load_file("ba1f")
    with open(filename) as f:
        genome = f.readline().strip()
    
    print(minimum_skew(genome))