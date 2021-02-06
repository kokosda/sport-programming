# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(node, height):
            if not node:
                return height
            
            h1, h2 = -1, -1
            
            if node.left:
                h1 = dfs(node.left, height + 1)
            if node.right:
                h2 = dfs(node.right, height + 1)
            
            if h1 == h2 == -1:
                return height
            
            if h1 == -1:
                return h2
            
            if h2 == -1:
                return h1
            
            return min(h1, h2)
        
        return dfs(root, 1)