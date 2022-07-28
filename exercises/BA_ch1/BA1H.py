import os
from exercises.utils import load_file
from exercises import BA1G

def approx_pattern_matching(pattern: str, text: str, d: int) -> str:
    """Find all approximate occurences of a pattern in a string
    
    We say that a k-mer Pattern appears as a substring of Text with at most d 
    mismatches if there is some k-mer substring Pattern of Text having d or fewer 
    mismatches with Pattern, i.e., HAMMINGDISTANCE(Pattern, Pattern') <= d.

    Parameters
    ----------
    pattern : str
        pattern to find
    text : str
        string to find the pattern to
    d : int
        maximum number of mismatches allowed

    Returns
    -------
    str
        string with all the starting positions where pattern appears as a 
        subtring of text with at most d mismatches
    """
    positions = []
    
    for i in range(0, len(text)-len(pattern)+1):
        mismatches = BA1G.hamming_distance(pattern, text[i:i+len(pattern)]) 
        if mismatches <= d:
            positions.append(i)
    
    return " ".join([str(x) for x in positions])
            
if __name__ == "__main__":
    filename = load_file("ba1h")
    with open(filename) as f:
        pattern = f.readline().strip()
        text = f.readline().strip()
        d = int(f.readline().strip())
    
    print(approx_pattern_matching(pattern, text, d))