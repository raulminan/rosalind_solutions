from exercises import utils

def overlap_graph(patterns: list):
    """Constructs the overlap graph of a collection of k-mers

    Parameters
    ----------
    patterns : list
        list of kmers
    """
    graph = []
    patterns = sorted(patterns)
    for i in range(len(patterns)):
        pattern = patterns[i]
        new_patterns = patterns[:i] + patterns[i+1:] # remove current kmer
        for j in range(len(new_patterns)):
            pattern2 = new_patterns[j]
            if pattern[1:] == pattern2[:-1]:
                graph.append(f"{pattern} -> {pattern2}")
    return graph

if __name__ == "__main__":
    filename = utils.load_file("ba3c")
    with open(filename) as f:
        patterns = f.read().splitlines()
    
    graph = overlap_graph(patterns)
    print("\n".join(graph))
