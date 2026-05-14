'''
Day73:- Dijkstra's algorithm
Difficulty:- Hard
Concept:- Greedy Algorithm , Priority Queue , Shortest Path
Approach:
Step 1 : Start from source node
Step 2 : Pick minimum distance node
Step 3 : Update neighbor distances
Step 4 : Repeat until all nodes processed

'''


import heapq

graph = {
    'A':[('B',1),('C',4)],
    'B':[('C',2),('D',5)],
    'C':[('D',1)],
    'D':[]
}

distance = {
    'A':0,
    'B':float('inf'),
    'C':float('inf'),
    'D':float('inf')
}

pq = [(0,'A')]

while pq:

    dist, node = heapq.heappop(pq)

    for neighbor, weight in graph[node]:

        new_dist = dist + weight

        if new_dist < distance[neighbor]:

            distance[neighbor] = new_dist

            heapq.heappush(pq, (new_dist, neighbor))

print(distance)



