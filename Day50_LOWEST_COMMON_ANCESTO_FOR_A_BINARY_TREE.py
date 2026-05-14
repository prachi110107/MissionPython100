'''
Day50:- Lowest common ancesto for a binary tree
Difficulty:- Hard
Concept:- Binary tree , recursion , tree traversal
Approach:
Step 1 : Start traversal from root node.
Step 2 : If root becomes : node1 , node2 , then return root.
Step 3 : Recursively search in : left subtree , right subtree
Step 4 : If both sides return values : current root is LCA
Step 5 : Otherwise return non-null subtree result.

'''

# Lowest Common Ancestor in Binary Tree

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# LCA Function
def lca(root, n1, n2):

    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root

    left = lca(root.left, n1, n2)
    right = lca(root.right, n1, n2)

    # if both found
    if left and right:
        return root

    # otherwise return non-null value
    if left:
        return left
    else:
        return right


# Creating Tree
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)


result = lca(root, 4, 5)

print("Lowest Common Ancestor is:", result.data)