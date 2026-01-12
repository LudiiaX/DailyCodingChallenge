import copy

def calcul_voisins(i, j, grid):
    maxi = len(grid)
    mini = 0
    voisins = [
        [0,1],
        [1,0],
        [1,1],
        [-1,0],
        [0,-1],
        [-1,-1],
        [-1,1],
        [1,-1],
    ]
    res = 0

    for v in voisins:
        ti = i + v[0]
        tj = j + v[1]
        if mini <= ti and mini <= tj and ti < maxi and tj < maxi:
            res += grid[ti][tj]
    return res




def game_of_life(grid):

    new = copy.deepcopy(grid)


    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res = calcul_voisins(i, j, grid)
            if grid[i][j] == 1 and res < 2:
                new[i][j] = 0
            if grid[i][j] == 1 and res > 3:
                new[i][j] = 0
            if grid[i][j] == 0 and res == 3:
                new[i][j] = 1
    return new

print(game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]))
print(game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]))
print(game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]))
