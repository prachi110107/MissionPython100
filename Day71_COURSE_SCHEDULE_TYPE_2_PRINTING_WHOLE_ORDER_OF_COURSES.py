'''
Day71:- Course schedule type 2 printing whole order of courses
Difficulty:- Hard
Concept:- BFS , Topological Sorting
Approach:
Step 1 : Perform Kahn's algorithm
Step 2 : Store traversal order
Step 3 : Print complete course order

'''


# Course Schedule II

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

# insert nodes with indegree 0
for i in range(numCourses):

    if indegree[i] == 0:
        queue.append(i)

order = []

while queue:

    node = queue.popleft()

    order.append(node)

    for neighbor in graph[node]:

        indegree[neighbor] -= 1

        if indegree[neighbor] == 0:
            queue.append(neighbor)

# print order
if len(order) == numCourses:
    print("Course Order:", order)
else:
    print("No valid order possible")