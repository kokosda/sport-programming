# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        res = True
        
        def dfs(node: TreeNode) -> bool:
            nonlocal val
            nonlocal res
            
            if node is None:
                return
            
            if res is False:
                return
            
            if node.val != val:
                res = False
                
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)        
        return res