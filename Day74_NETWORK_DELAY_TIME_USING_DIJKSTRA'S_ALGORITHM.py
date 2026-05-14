'''
Day74:- Network delay time using Dijkstra's algorithm
Difficulty:- Hard
Concept:- Graphs , Dijkstra's Algorithm , Priority Queue (Min Heap) , Shortest Path
Approach:
Step 1 : Create graph using adjacency list.
Step 2 : Store : (source, destination, time)
Step 3 : Use a priority queue to always select the node with minimum time.
Step 4 : Update shortest travel time for neighboring nodes.
Step 5 : Find maximum time among all shortest paths : if all nodes visited → return maximum time
                                                 otherwise ,  return -1

'''

# Network Delay Time using Dijkstra's Algorithm

import heapq

times = [
    [2,1,1],
    [2,3,1],
    [3,4,1]
]

n = 4
k = 2

# create graph
graph = {}

for u, v, w in times:

    if u not in graph:
        graph[u] = []

    graph[u].append((v, w))


# priority queue
pq = [(0, k)]

# shortest distances
visited = {}

while pq:

    time, node = heapq.heappop(pq)

    if node in visited:
        continue

    visited[node] = time

    if node in graph:

        for neighbor, weight in graph[node]:

            if neighbor not in visited:

                new_time = time + weight

                heapq.heappush(pq, (new_time, neighbor))


# check all nodes reached
if len(visited) == n:

    print("Network Delay Time:", max(visited.values()))

else:
    print(-1)