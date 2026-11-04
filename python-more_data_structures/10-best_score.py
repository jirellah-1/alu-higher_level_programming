#!/usr/bin/python3
def best_score(a_dictionary):
     """Return the key with the highest integer value."""
    if not a_dictionary:
        return None

    best_key = None
    highest_score = None

    for key, score in a_dictionary.items():
        if highest_score is None or score > highest_score:
            highest_score = score
            best_key = key

    return best_key

