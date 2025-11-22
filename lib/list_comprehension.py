def return_evens(sequence):
    """
    Return a list of all even numbers in the sequence.
    Uses a list comprehension.
    """
    return [n for n in sequence if n % 2 == 0]


def make_exclamation(sentences):
    """
    Return a list of sentences with an exclamation mark added.
    Uses a list comprehension.
    """
    return [sentence + "!" for sentence in sentences]

