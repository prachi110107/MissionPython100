'''
Day51:- Diameter of binary tree
Difficulty:- Hard
Concept:- Binary Trees , Recursion , Height Calculation
Approach:
Step 1 : Find left subtree height
Step 2 : Find right subtree height
Step 3 : Diameter = left height + right height
Step 4 : Update maximum diameter recursively

'''

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

diameter = 0

def height(root):

    global diameter

    if root is None:
        return 0

    left = height(root.left)
    right = height(root.right)

    diameter = max(diameter, left + right)

    return max(left, right) + 1


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

height(root)

print("Diameter is:", diameter)