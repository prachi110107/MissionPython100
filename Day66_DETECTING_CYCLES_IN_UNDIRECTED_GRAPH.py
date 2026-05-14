'''
Day66:- Detecting cycles in undirected graph
Difficulty:- Hard
Concept:- DFS , Visited Array , Parent Tracking
Approach:
Step 1 : Traverse graph using DFS
Step 2 : Mark visited nodes
Step 3 : If visited neighbor is not parent : cycle exists

'''

graph = {
    0:[1],
    1:[0,2],
    2:[1,3],
    3:[2,1]
}

visited = set()

def dfs(node, parent):

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:

            if dfs(neighbor, node):
                return True

        elif neighbor != parent:
            return True

    return False

print(dfs(0, -1))