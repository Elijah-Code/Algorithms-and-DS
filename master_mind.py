"""
Cracking the coding interview 16.15
"""

def hits(guess, solution):
    """
    0 - pseudo-hit
    1 - hit
    """
    num_h = 0
    num_ph = 0

    for letter_ix in range(len(solution)):
        if solution[letter_ix] == guess[letter_ix]:
            num_h += 1
        elif solution[letter_ix] in guess:
            num_ph += 1

    return num_h, num_ph


print(hits("GGRY", "RGYG"))
