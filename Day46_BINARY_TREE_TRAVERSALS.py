'''
Day46:- Binary tree traversals
Difficulty:- Hard
Concept:- Binary Trees , Recursion , Queue (for level order traversal)
Approach:
Step 1 : Create nodes and connect them to form a binary tree.
Step 2 : For Preorder:Root → Left → Right
Step 3 : For Inorder:Left → Root → Right
Step 4 : For Postorder:Left → Right → Root
Step 5 : For Level Order:Use queue , Traverse tree level by level

'''

# Binary Tree Traversals

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Preorder Traversal
def preorder(root):

    if root:
        print(root.data, end=" ")

        preorder(root.left)
        preorder(root.right)


# Inorder Traversal
def inorder(root):

    if root:
        inorder(root.left)

        print(root.data, end=" ")

        inorder(root.right)


# Postorder Traversal
def postorder(root):

    if root:
        postorder(root.left)
        postorder(root.right)

        print(root.data, end=" ")


# Level Order Traversal
def levelorder(root):

    queue = []

    queue.append(root)

    while queue:

        node = queue.pop(0)

        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


# Creating Binary Tree
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)


print("Preorder Traversal:")
preorder(root)

print("\nInorder Traversal:")
inorder(root)

print("\nPostorder Traversal:")
postorder(root)

print("\nLevel Order Traversal:")
levelorder(root)