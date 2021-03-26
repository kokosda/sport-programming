"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        stack = [root]
        res = []
        
        while len(stack) > 0:
            node = stack.pop()
            res.append(node.val)
            
            for child in reversed(node.children):
                stack.append(child)
            
        return res