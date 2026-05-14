'''
Day54:- Check if two trees are identical using recursion
Difficulty:- Hard
Concept:- Recursion , Tree Comparison
Approach:
Step 1 : Compare root values
Step 2 : Recursively compare : left subtree , right subtree
Step 3 : Return True if all nodes match

'''

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def identical(root1, root2):

    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return (root1.data == root2.data and
            identical(root1.left, root2.left) and
            identical(root1.right, root2.right))


root1 = Node(1)
root1.left = Node(2)

root2 = Node(1)
root2.left = Node(2)

print(identical(root1, root2))