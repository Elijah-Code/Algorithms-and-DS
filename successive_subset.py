"""
GeeksForGeeks

https://www.geeksforgeeks.org/longest-consecutive-subsequence/
"""

def get_consecutive_subset(arr, ix):
    subset_len=1
    while arr[ix] + 1 == arr[ix+1]:
        ix += 1
        subset_len += 1
    return subset_len

def consecutive_subset(arr, ix=0):
    if ix >= len(arr): return 0
    if len(arr) == ix+1: return 1
    
    l = get_consecutive_subset(arr, ix)
    return max(l, consecutive_subset(arr, ix=ix+l))




arr = [1,4,6,1,2,3,4,7,5,8,3,4,5,6,7,23,4,27,8,9,23,24,25,26,27,24,6,82,54245]

arr = [1,1,2,3,4,3,4,53,6]

print(consecutive_subset(arr))