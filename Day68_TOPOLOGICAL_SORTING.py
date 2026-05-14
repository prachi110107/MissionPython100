'''
Day68:- Topological sorting
Difficulty:- Hard
Concept:- DFS , Stack , DAG
Approach:
Step 1 : Perform DFS
Step 2 : Push nodes into stack after recursion
Step 3 : Reverse stack gives topological order

'''

graph = {
    5:[2,0],
    4:[0,1],
    2:[3],
    3:[1],
    1:[],
    0:[]
}

visited = set()

stack = []

def dfs(node):

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:
            dfs(neighbor)

    stack.append(node)

for node in graph:

    if node not in visited:
        dfs(node)

stack.reverse()

print(stack)