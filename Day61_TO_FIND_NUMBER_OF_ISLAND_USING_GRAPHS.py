'''
Day61:- To find number of island using graphs
Difficulty:- Hard
Concept:- Graph Traversal , DFS , Matrix Traversal
Approach:
Step 1 : Traverse matrix
Step 2 : If land (1) found : increase island count , perform DFS
Step 3 : Mark connected land as visited

'''

grid = [
    ["1","1","0"],
    ["1","0","0"],
    ["0","1","1"]
]

rows = len(grid)
cols = len(grid[0])

count = 0

def dfs(r, c):

    if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
        return

    grid[r][c] = "0"

    dfs(r+1, c)
    dfs(r-1, c)
    dfs(r, c+1)
    dfs(r, c-1)


for i in range(rows):

    for j in range(cols):

        if grid[i][j] == "1":

            count += 1
            dfs(i, j)

print("Number of islands:", count)