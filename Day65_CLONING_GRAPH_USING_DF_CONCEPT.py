'''
Day65:- cloning graph using DF concept 
Difficulty:- Hard
Concept:- DFS , HashMap , Graph Copying
Approach:
Step 1 : Create copy node
Step 2 : Store old-new mapping
Step 3 : Recursively clone neighbors

'''

class Node:

    def __init__(self, val):
        self.val = val
        self.neighbors = []


visited = {}

def clone(node):

    if node in visited:
        return visited[node]

    copy = Node(node.val)

    visited[node] = copy

    for neighbor in node.neighbors:
        copy.neighbors.append(clone(neighbor))

    return copy