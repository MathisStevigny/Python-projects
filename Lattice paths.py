#How many such routes are there through a 20×20 grid?
l = 20
x = l + 1
y = 1
#Setup grid
gridRowPath = [2 for column in range(l+1)]
gridRowPath.insert(0,1)
gridRowPath.append(1)
gridRowBoarder = [1 for column in range(l+3)]
grid = [[0 for column in range(l)]
for row in range(l)]
for row in grid:
    row.insert(0,1)
    row.insert(1,2)
    row.append(1)
grid.append(gridRowPath)
grid.append(gridRowBoarder)
grid.insert(0,gridRowBoarder)
for row in grid:
    print(row)

#Checks
while y < y+1:
    if grid[y+1][x] != 2:
        if grid[y][x-1] != 2:
            pass