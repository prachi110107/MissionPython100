'''
Day47:- Level traversal BFS 
Difficulty:- Hard
Concept:- Binary Trees , Breadth First Search (BFS) , Queue Data Structure
Approach:
Step 1 : Create a binary tree with nodes.
Step 2 : Use a queue and insert the root node into it.
Step 3 : Remove the front node from the queue and print it.
Step 4 : Insert the left child and right child of that node into the queue.
Step 5 : Repeat the process until the queue becomes empty.

'''


# Level Order Traversal using BFS

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# BFS Traversal Function
def level_order(root):

    if root is None:
        return

    queue = []

    # insert root node
    queue.append(root)

    while queue:

        # remove front node
        node = queue.pop(0)

        print(node.data, end=" ")

        # insert left child
        if node.left:
            queue.append(node.left)

        # insert right child
        if node.right:
            queue.append(node.right)


# Creating Binary Tree
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)


print("Level Order Traversal:")

level_order(root)