'''
Day59:- Boundary traversal of binary tree
Difficulty:- Hard
Concept:- Tree Traversal , Left Boundary , Leaf Nodes , Right Boundary
Approach:
Step 1 : Print root
Step 2 : Print left boundary
Step 3 : Print all leaf nodes
Step 4 : Print right boundary in reverse

'''

# Boundary Traversal of Binary Tree

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Print left boundary
def leftBoundary(root):

    current = root.left

    while current:

        if current.left or current.right:
            print(current.data, end=" ")

        if current.left:
            current = current.left
        else:
            current = current.right


# Print leaf nodes
def leafNodes(root):

    if root is None:
        return

    leafNodes(root.left)

    if root.left is None and root.right is None:
        print(root.data, end=" ")

    leafNodes(root.right)


# Print right boundary
def rightBoundary(root):

    current = root.right

    stack = []

    while current:

        if current.left or current.right:
            stack.append(current.data)

        if current.right:
            current = current.right
        else:
            current = current.left

    while stack:
        print(stack.pop(), end=" ")


# Boundary Traversal
def boundaryTraversal(root):

    if root is None:
        return

    print(root.data, end=" ")

    leftBoundary(root)

    leafNodes(root)

    rightBoundary(root)


# Creating Tree
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

print("Boundary Traversal:")

boundaryTraversal(root)