'''
Day63:- Flood fill algorithm DFS
Difficulty:- Hard
Concept:- DFS , Matrix Traversal , Recursion
Approach:
Step 1 : Start from source pixel
Step 2 : Change current color
Step 3 : Recursively fill neighboring cells

'''

image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]

sr = 1
sc = 1
newColor = 2

old = image[sr][sc]

rows = len(image)
cols = len(image[0])

def dfs(r, c):

    if r < 0 or c < 0 or r >= rows or c >= cols:
        return

    if image[r][c] != old:
        return

    image[r][c] = newColor

    dfs(r+1, c)
    dfs(r-1, c)
    dfs(r, c+1)
    dfs(r, c-1)

dfs(sr, sc)

print(image)