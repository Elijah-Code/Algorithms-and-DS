"""
Cracking the code interview - 17.18
"""
import math

def max_supersequence(sub, arr):
    indexes = {
        val: [] for val in sub
    }
    
    # O(n)
    for ix in range(len(arr)):
        if arr[ix] in indexes:
            indexes[arr[ix]].append(ix)


    # start and end of subsequence
    sub_ix = [-math.inf, math.inf]

    while True: # O(n)
        min_num = None
        min_ix = math.inf
        max_ix = 0

        for key, l in indexes.items(): # O(m)
            if l[0] < min_ix:
                min_ix = l[0]
                min_num = key
            if l[0] > max_ix:
                max_ix = l[0]

        if sub_ix[1] - sub_ix[0] > max_ix - min_ix:
            sub_ix[0] = min_ix
            sub_ix[1] = max_ix
        indexes[min_num].pop(0)

        if not indexes[min_num]:
            break

    return sub_ix

sub = [7,9,2]
arr = [1,4,9,7,3,5,2,7,9,1,4]
    
print(max_supersequence(sub, arr))
