'''
Day57:- Binary tree right side view using BFS traversal
Difficulty:- Hard
Concept:- BFS Traversal , Queue
Approach:
Step 1 : Traverse level by level
Step 2 : Reverse alternate levels

'''

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def rightView(root):

    queue = [root]

    while queue:

        size = len(queue)

        for i in range(size):

            node = queue.pop(0)

            if i == size - 1:
                print(node.data, end=" ")

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)


root = Node(1)

root.left = Node(2)
root.right = Node(3)

rightView(root)