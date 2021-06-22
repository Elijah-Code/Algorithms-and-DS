def kill_ship(mat, i, j):
    # Horizontal
    while j <= len(mat[0])-1 and mat[i][j+1]:
        mat[i][j] = 0
        j += 1
    
    # vertical
    while i <= len(mat) - 1 and mat[i+1][j]:
        mat[i][j] = 0
        i += 1

def count_ships(mat):
    c = 0

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]:
                c += 1
                kill_ship(mat, i, j)

    return c
    

sea = [
    [0,0,0,1],
    [0,0,0,1],
    [1,1,0,1],
    [0,0,0,0],
]

ships = 0
for i in range(len(sea)):
    for j in range(len(sea[0])):

        if sea[i][j] == 1:
            if i != len(sea)-1:
                if (i == 0 or sea[i-1][j] == 0) and (sea[i+1][j] == 1):
                    ships += 1

            if j != len(sea[0])-1:
                if (sea[i][j+1] == 1) and (j == 0 or sea[i][j-1] == 0):
                    ships += 1

print(ships)


