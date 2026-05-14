'''
Day70:- Course schedule using khan's algorithm
Difficulty:- Hard
Concept:- Topological Sort , BFS , Indegree
Approach:
Step 1 : Build graph
Step 2 : Calculate indegree
Step 3 : Perform BFS topological sort
Step 4 : If all courses visited : possible

'''

# Course Schedule using Kahn's Algorithm

from collections import deque

numCourses = 4

prerequisites = [
    [1,0],
    [2,0],
    [3,1],
    [3,2]
]

# create graph
graph = {i: [] for i in range(numCourses)}

# indegree array
indegree = [0] * numCourses

# build graph
for course, prereq in prerequisites:

    graph[prereq].append(course)

    indegree[course] += 1


queue = deque()

# insert indegree 0 nodes
for i in range(numCourses):

    if indegree[i] == 0:
        queue.append(i)

count = 0

while queue:

    node = queue.popleft()

    count += 1

    for neighbor in graph[node]:

        indegree[neighbor] -= 1

        if indegree[neighbor] == 0:
            queue.append(neighbor)

# check possible or not
if count == numCourses:
    print("Possible to finish all courses")
else:
    print("Not possible")