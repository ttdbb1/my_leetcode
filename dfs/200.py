grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

def numIslands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(int(grid[i][j]) == 1):
                count += 1
                com_num(grid, i, j)
    return count

def check(grid, x, y):
    return x >= 0 and x<= len(grid) - 1 and y >= 0 and y <= len(grid[0]) - 1


def com_num(grid, x, y):
    if not check(grid, x, y):
        return 0
    if int(grid[x][y]) != 1:
        return 0
    grid[x][y] = str(2)
    com_num(grid, x - 1, y)
    com_num(grid, x + 1, y)
    com_num(grid, x, y - 1)
    com_num(grid, x, y + 1)
print(numIslands(grid))