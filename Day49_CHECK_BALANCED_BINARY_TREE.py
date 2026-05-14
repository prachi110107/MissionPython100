'''
Day49:- Check balanced binary tree
Difficulty:- Hard
Concept:- Binary Trees , Recursion , Height Calculation
Approach:
Step 1 : Find height of left subtree.
Step 2 : Find height of right subtree.
Step 3 : Calculate difference : abs(left_height - right_height)
Step 4 : If difference is greater than 1 : Tree is not balanced
Step 5 : Recursively check left and right subtrees.

'''

# Check Balanced Binary Tree

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to find height
def height(root):

    if root is None:
        return 0

    left = height(root.left)
    right = height(root.right)

    return max(left, right) + 1


# Function to check balance
def isBalanced(root):

    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return isBalanced(root.left) and isBalanced(root.right)


# Creating Tree
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

# Check balance
if isBalanced(root):
    print("Balanced Binary Tree")
else:
    print("Not Balanced")