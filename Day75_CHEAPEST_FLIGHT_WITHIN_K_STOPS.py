'''
Day75:- Cheapest flight within K stops
Difficulty:- Hard
Concept:- Graphs , BFS , Priority Queue , Shortest Path
Approach:
Step 1 : Create graph using adjacency list.
Step 2 : Store : (source, destination, price)
Step 3 : Use queue to store : current node , total cost , number of stops
Step 4 : Traverse neighbors until stops ≤ k.
Step 5 : Update minimum flight cost.

'''


# Cheapest Flight Within K Stops

from collections import deque

n = 4

flights = [
    [0,1,100],
    [1,2,100],
    [2,3,100],
    [0,2,500]
]

src = 0
dst = 3
k = 1

# create graph
graph = {}

for u, v, w in flights:

    if u not in graph:
        graph[u] = []

    graph[u].append((v, w))


queue = deque()

queue.append((src, 0, 0))

minimum = float("inf")

while queue:

    node, cost, stops = queue.popleft()

    if node == dst:
        minimum = min(minimum, cost)

    if stops > k:
        continue

    if node in graph:

        for neighbor, price in graph[node]:

            queue.append((neighbor,
                          cost + price,
                          stops + 1))


if minimum == float("inf"):
    print(-1)
else:
    print("Cheapest Cost:", minimum)
