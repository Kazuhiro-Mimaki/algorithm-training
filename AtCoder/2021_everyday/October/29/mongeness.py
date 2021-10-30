H, W = input().strip().split()
H, W = [int(H), int(W)]

grid = []
for i in range(H):
    array = list(map(int, input().strip().split()))
    grid.append(array)


def check():
    for i1 in range(H-1):
        for i2 in range(i1+1, H):
            for j1 in range(W-1):
                for j2 in range(j1+1, W):
                    A_i1_j1 = grid[i1][j1]
                    A_i1_j2 = grid[i1][j2]
                    A_i2_j1 = grid[i2][j1]
                    A_i2_j2 = grid[i2][j2]
                    if A_i1_j1 + A_i2_j2 > A_i1_j2 + A_i2_j1:
                        return False
    return True


print('Yes') if check() else print('No')
