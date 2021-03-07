"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        def dfs(node: Node, level: int) -> int:
            if node is None:
                return level
            
            depth = level
            
            for child in node.children:
                depth = max(depth, dfs(child, level + 1))
                
            return depth
        
        res = dfs(root, level=1)
        return res