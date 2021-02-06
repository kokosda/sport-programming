# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def dfs(node, height):
            if not node:
                return height
            
            h1 = dfs(node.left, height + 1)
            h2 = dfs(node.right, height + 1)
            
            if abs(h1 - h2) > 1:
                return -1
            
            return max(h1, h2)
        
        hleft = dfs(root.left, 0)
        hright = dfs(root.right, 0)
        
        if hleft == -1 or hright == -1:
            return False
        
        return abs(hleft - hright) <= 1