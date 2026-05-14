'''
Day69:- Topological sort using BFS (khan's algorithm)
Difficulty:- Hard
Concept:- BFS , Queue , Indegree
Approach:
Step 1 : Calculate indegree of every node
Step 1 : Insert nodes with indegree 0 into queue
Step 1 : Remove node and reduce indegree of neighbors

'''

from collections import deque

graph = {
    5:[2,0],
    4:[0,1],
    2:[3],
    3:[1],
    1:[],
    0:[]
}

indegree = {i:0 for i in graph}

for node in graph:

    for neighbor in graph[node]:
        indegree[neighbor] += 1

queue = deque()

for node in indegree:

    if indegree[node] == 0:
        queue.append(node)

result = []

while queue:

    node = queue.popleft()

    result.append(node)

    for neighbor in graph[node]:

        indegree[neighbor] -= 1

        if indegree[neighbor] == 0:
            queue.append(neighbor)

print(result)