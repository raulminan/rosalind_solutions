import os

def pattern_count(text, pattern) -> int:
    """Compute the number of times a pattern appears in a text

    Parameters
    ----------
    text : str
        string where we want to find the pattern in
    pattern : str
        pattern we want to find

    Returns
    -------
    int
        number of times the pattern appears in the text
    """
    count = 0
    for i in range(0, len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "rosalind_ba1a.txt")
    with open(filename) as f:
        text = f.readline().strip()
        pattern = f.readline().strip()
        
    print(pattern_count(text, pattern))

