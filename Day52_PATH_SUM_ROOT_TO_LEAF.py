'''
Day52:- Path sum root to leaf
Difficulty:- Hard
Concept:- Binary Trees , Recursion , DFS traversal
Approach:
Step 1 : Traverse tree recursively
Step 2 : Add node values to sum
Step 3 : If leaf node reached : compare with target sum
Step 4 : Return True or False


'''

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pathSum(root, target):

    if root is None:
        return False

    if root.left is None and root.right is None:
        return target == root.data

    target = target - root.data

    return pathSum(root.left, target) or pathSum(root.right, target)


root = Node(5)

root.left = Node(4)
root.right = Node(8)

root.left.left = Node(11)

print(pathSum(root, 20))