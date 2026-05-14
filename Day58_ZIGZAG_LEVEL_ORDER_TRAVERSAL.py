'''
Day58:- ZIGZAG level order traversal
Difficulty:- Hard
Concept:- BFS , Queue , Alternate Reversal
Approach:
Step 1 : Traverse level by level
Step 2 : Reverse alternate levels

'''

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def zigzag(root):

    queue = [root]

    left_to_right = True

    while queue:

        size = len(queue)

        level = []

        for i in range(size):

            node = queue.pop(0)

            level.append(node.data)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        if not left_to_right:
            level.reverse()

        print(level)

        left_to_right = not left_to_right


root = Node(1)

root.left = Node(2)
root.right = Node(3)

zigzag(root)