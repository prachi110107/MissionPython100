'''
Day60:- Verticle order traversal using trees dictionaries hashmap
Difficulty:- Hard
Concept:- BFS , HashMap / Dictionary , Horizontal Distance
Approach:
Step 1 : Assign horizontal distance to each node
Step 2 : Store nodes in dictionary
Step 3 : Traverse level by level
Step 4 : Print nodes column wise

'''

# Vertical Order Traversal

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def verticalOrder(root):

    if root is None:
        return

    # dictionary for storing nodes
    hashmap = {}

    # queue stores node and horizontal distance
    queue = [(root, 0)]

    while queue:

        node, hd = queue.pop(0)

        if hd in hashmap:
            hashmap[hd].append(node.data)
        else:
            hashmap[hd] = [node.data]

        # left child
        if node.left:
            queue.append((node.left, hd - 1))

        # right child
        if node.right:
            queue.append((node.right, hd + 1))

    # print vertical order
    for key in sorted(hashmap):

        print(hashmap[key])


# Creating Tree
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

print("Vertical Order Traversal:")

verticalOrder(root)