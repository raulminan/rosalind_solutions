from exercises.utils import load_file

def hamming_distance(p: str, q: str) -> int:
    """Computes the hamming distance betwwen two strings of equal length
    
    We say that position i in k-mers p1...pk and q1...qk is a mismatch if p_i != q_i. 
    Thenumber of mismatches between strings p and q is called the Hamming distance 
    between these strings and is denoted HAMMINGDISTANCE(p, q).

    Parameters
    ----------
    p : str
        first string
    q : str
        second string

    Returns
    -------
    int
        hamming distance
    """
    distance = 0
    for i in range(len(q)):
        if q[i] != p[i]:
            distance += 1
    
    return distance

if __name__ == "__main__":
    filename = load_file("ba1g")
    with open(filename) as f:
        q = f.readline().strip()
        p = f.readline().strip()
    
    print(hamming_distance(p, q))