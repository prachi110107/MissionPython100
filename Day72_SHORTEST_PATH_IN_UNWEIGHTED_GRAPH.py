'''
Day72:- Shortest path in unweighted graph
Difficulty:- Hard
Concept:- BFS , Queue , Distance Array
Approach:
Step 1 : Start BFS from source
Step 2 : Update distance of neighbors
Step 3 : First visit gives shortest path

'''

from collections import deque

graph = {
    0:[1,2],
    1:[3],
    2:[3],
    3:[]
}

queue = deque([0])

distance = {0:0}

while queue:

    node = queue.popleft()

    for neighbor in graph[node]:

        if neighbor not in distance:

            distance[neighbor] = distance[node] + 1

            queue.append(neighbor)

print(distance)