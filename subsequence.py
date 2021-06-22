"""
Algoexpert

https://www.algoexpert.io/questions/Validate%20Subsequence
"""


def isValidSubsequence(array, sequence):
    if len(sequence) == 1 and sequence[0] in array:
        return True

    for seq_ix in range(len(sequence)):
        for num_ix in range(len(array)):
            if array[num_ix] == sequence[seq_ix]:
                return isValidSubsequence(array[(num_ix+1):], sequence[(seq_ix+1):])
    return False

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [25]

print(isValidSubsequence(array, sequence))


