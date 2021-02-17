# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, p, q):
            if not node:
                return None
            
            if p.val < node.val and q.val < node.val:
                return dfs(node.left, p, q)
            elif p.val > node.val and q.val > node.val:
                return dfs(node.right, p, q)
            else:
                return node
                
        return dfs(root, p, q)
    
"""
p, q
k - общий родитель
k==p or k==q
p - 0, q - 5
"""