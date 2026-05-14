'''
Day56:- Maximum path sum binary tree harder version
Difficulty:- Hard
Concept:- Recursion , DFS , Dynamic Path Calculation
Approach:
Step 1 : Find maximum left path sum
Step 2 : Find maximum right path sum
Step 3 : Ignore negative sums
Step 4 : Update global maximum path sum

'''

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


maximum = float("-inf")


def pathSum(root):

    global maximum

    if root is None:
        return 0

    left = max(pathSum(root.left), 0)
    right = max(pathSum(root.right), 0)

    current = root.data + left + right

    maximum = max(maximum, current)

    return root.data + max(left, right)


root = Node(10)

root.left = Node(2)
root.right = Node(10)

root.left.left = Node(20)
root.left.right = Node(1)

pathSum(root)

print("Maximum Path Sum:", maximum)