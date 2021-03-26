# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(node, lp, rp) -> int:            
            diff = min(abs(node.val - lp.val), abs(node.val - rp.val))
            
            if node.left:
                diff = min(diff, dfs(node.left, lp, node))
                
            if node.right:
                diff = min(diff, dfs(node.right, node, rp))
                
            return diff
        
        diff1, diff2 = None, None
        
        if root.left:
            diff1 = dfs(root.left, root, root)
            
        if root.right:
            diff2 = dfs(root.right, root, root)
        
        return min(diff1, diff2) if diff1 and diff2 else diff1 or diff2
    
"""
[5,1,18,null,3,16,29,null,null,7]
"""