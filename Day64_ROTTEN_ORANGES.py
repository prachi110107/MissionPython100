'''
Day64:- Rotten oranges
Difficulty:- Hard
Concept:- BFS , Queue , Multi-source Traversal
Approach:
Step 1 : Insert all rotten oranges into queue
Step 2 : Traverse neighbors level by level
Step 3 : Convert fresh oranges into rotten
Step 4 : Count minutes

'''

from collections import deque

grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]

rows = len(grid)
cols = len(grid[0])

queue = deque()

fresh = 0
time = 0

for i in range(rows):

    for j in range(cols):

        if grid[i][j] == 2:
            queue.append((i,j))

        elif grid[i][j] == 1:
            fresh += 1

directions = [[1,0],[-1,0],[0,1],[0,-1]]

while queue and fresh > 0:

    for i in range(len(queue)):

        r, c = queue.popleft()

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:

                grid[nr][nc] = 2

                queue.append((nr,nc))

                fresh -= 1

    time += 1

print("Minutes:", time)