from math import factorial

N = int(input())
xy_grid = []
for i in range(1, N+1):
    xy_grid.append(list(map(int, input().strip().split())))

ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            x1, y1 = xy_grid[i]
            x2, y2 = xy_grid[j]
            x3, y3 = xy_grid[k]
            if (x2-x1)*(y3-y1) != (x3-x1)*(y2-y1):
                ans += 1

print(ans)
