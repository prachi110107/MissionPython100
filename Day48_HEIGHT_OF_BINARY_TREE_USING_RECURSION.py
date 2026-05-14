'''
Day48:- Height of binary tree using recursion
Difficulty:- Hard
Concept:- Binary Trees , Recursion , Depth Calculation
Approach:
Step 1 : Create nodes and form the binary tree.
Step 2 : Use recursion to find : height of left subtree , height of right subtree
Step 3 : Find maximum of left and right height.
Step 4 : Add 1 for current node.
Step 5 : Return the final height of the tree.

'''


# Height of Binary Tree using Recursion

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to find height
def height(root):

    # base condition
    if root is None:
        return 0

    # find left subtree height
    left_height = height(root.left)

    # find right subtree height
    right_height = height(root.right)

    # return maximum height
    return max(left_height, right_height) + 1


# Creating Binary Tree
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)


print("Height of binary tree is:", height(root))