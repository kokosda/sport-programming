"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        stack = [root]
        res = []
        already_added = set()
        
        while len(stack) > 0:
            node = stack[-1]
            
            if node not in already_added:            
                for child in reversed(node.children):
                    stack.append(child)
                
                if node.children:
                    already_added.add(node)
                    continue
                
            child = stack.pop()
            res.append(child.val)
        
        return res