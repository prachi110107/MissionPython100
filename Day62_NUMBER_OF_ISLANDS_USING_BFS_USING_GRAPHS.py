'''
Day62:- Number of islands using BFS using graphs
Difficulty:- Hard
Concept:- BFS , Queue , Graph Traversal
Approach:
Step 1 : Traverse matrix
Step 2 : If land found : increment count , perform BFS using queue
Step 3 : Mark visited cells

'''

from collections import deque

grid = [
    ["1","1","0"],
    ["1","0","0"],
    ["0","1","1"]
]

rows = len(grid)
cols = len(grid[0])

count = 0

def bfs(r, c):

    queue = deque()

    queue.append((r, c))

    grid[r][c] = "0"

    while queue:

        row, col = queue.popleft()

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":

                queue.append((nr, nc))
                grid[nr][nc] = "0"


for i in range(rows):

    for j in range(cols):

        if grid[i][j] == "1":

            count += 1
            bfs(i, j)

print("Number of islands:", count)
