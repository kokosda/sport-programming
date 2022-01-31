from collections import deque
class Node:
	def __init__(self, info: int):
		self.info = info
		self.left = None
		self.right = None
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    stack = deque()
    stack.append(root)

    for node in get_next_node(stack):
        print(node.info, end=' ')

def get_next_node(stack: deque) -> Node:
    if len(stack) == 0:
        return None

    node = stack.pop()
    yield node

    if node.right:
        stack.append(node.right)

    if node.left:
        stack.append(node.left)

    yield from get_next_node(stack)

root = Node(5)
root.left = Node(3)
root.left.left = Node(9)
root.left.right = Node(14)
root.left.right.right = Node(2)
root.right = Node(7)

preOrder(root)