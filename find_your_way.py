import math
mat = [
    [2,0,0,0,0,0,0],
    [0,0,0,0,1,0,0],
    [0,1,0,1,0,0,0],
    [0,1,0,0,1,0,0],
    [0,0,0,3,0,0,0],
    [1,1,0,0,0,0,0],
]

mat = [
    [2,0,0,0,0,0,0],
    [1,1,0,0,1,0,0],
    [0,0,0,1,0,0,0],
    [0,1,0,1,1,0,0],
    [0,0,0,0,0,3,0],
    [0,0,0,0,0,0,0],
]

def find_way(mat, i, j):
    if i >= len(mat) or j >= len(mat[0]): return math.inf
    if mat[i][j] == 3: return 0
    if mat[i][j] == 1: return math.inf

    down = find_way(mat, i+1, j)
    right = find_way(mat, i, j+1)

    return min(down, right) + 1

print(find_way(mat, 0, 0))


