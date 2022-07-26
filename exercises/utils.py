"""utils functions for exercises"""
import os

def load_file(id: str) -> str:
    """Returns filename given a exercise id

    Parameters
    ----------
    exercise : str
        id of the exercise (e.g. ba1a)

    Returns
    -------
    str
        filepath to the exercise
    """
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", f"rosalind_{id}.txt")