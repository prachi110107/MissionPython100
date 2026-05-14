'''
Day53:- Maximum depth and minimum depth of binary tree
Difficulty:- Hard
Concept:- Recursion , Tree Height
Approach:
Step 1 : Recursively calculate left and right depth
Step 2 : Maximum depth : max(left, right) + 1
Step 3 : Minimum depth : min(left, right) + 1

'''

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxDepth(root):

    if root is None:
        return 0

    return max(maxDepth(root.left),
               maxDepth(root.right)) + 1


def minDepth(root):

    if root is None:
        return 0

    return min(minDepth(root.left),
               minDepth(root.right)) + 1


root = Node(1)

root.left = Node(2)
root.right = Node(3)

print("Maximum Depth:", maxDepth(root))
print("Minimum Depth:", minDepth(root))