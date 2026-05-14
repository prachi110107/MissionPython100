'''
Day55:- Symmetric tree
Difficulty:- Hard
Concept:- Mirror Trees , Recursion
Approach:
Step 1 : Compare left subtree with right subtree
Step 2 : Check : left.left == right.right
                 left.right == right.left

'''

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def mirror(left, right):

    if left is None and right is None:
        return True

    if left is None or right is None:
        return False

    return (left.data == right.data and
            mirror(left.left, right.right) and
            mirror(left.right, right.left))


def symmetric(root):

    return mirror(root.left, root.right)


root = Node(1)

root.left = Node(2)
root.right = Node(2)

print(symmetric(root))