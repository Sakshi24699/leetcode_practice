grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

grid1 = [[] for k in range(len(grid))]
cnt = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        grid1[i].append(grid[j][i])
for i in grid:
    for j in grid1:
        if i == j:
            cnt += 1
print(cnt)