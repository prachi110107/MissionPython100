'''
Day76:- Minimum spanning tree
Difficulty:- Hard
Concept:- Graphs , Greedy Algorithm , Priority Queue , Minimum Spanning Tree (MST)
Approach:
Step 1 : Start from any node.
Step 2 : Insert connected edges into priority queue.
Step 3 : Pick edge with minimum weight.
Step 4 : Add unvisited node into MST.
Step 5 : Repeat until all nodes are visited.

'''

# Minimum Spanning Tree using Prim's Algorithm

import heapq

graph = {
    0:[(1,2),(3,6)],
    1:[(0,2),(2,3),(3,8),(4,5)],
    2:[(1,3),(4,7)],
    3:[(0,6),(1,8)],
    4:[(1,5),(2,7)]
}

visited = set()

pq = [(0, 0)]

cost = 0

while pq:

    weight, node = heapq.heappop(pq)

    if node in visited:
        continue

    visited.add(node)

    cost += weight

    for neighbor, edge_weight in graph[node]:

        if neighbor not in visited:

            heapq.heappush(pq,
                           (edge_weight, neighbor))

print("Minimum Spanning Tree Cost:", cost)