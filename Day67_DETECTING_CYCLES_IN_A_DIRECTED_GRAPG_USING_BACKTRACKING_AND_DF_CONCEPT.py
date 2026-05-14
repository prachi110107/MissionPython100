'''
Day67:- Detecting cycles in a directed graph using backtracking and DF concept 
Difficulty:- Hard
Concept:- DFS , Backtracking , Recursion Stack
Approach:
Step 1 : Use visited set
Step 2 : Use recursion stack
Step 3 : If node already in recursion stack : cycle exists

'''
graph = {
    0:[1],
    1:[2],
    2:[0]
}

visited = set()

path = set()

def dfs(node):

    visited.add(node)

    path.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:

            if dfs(neighbor):
                return True

        elif neighbor in path:
            return True

    path.remove(node)

    return False

print(dfs(0))