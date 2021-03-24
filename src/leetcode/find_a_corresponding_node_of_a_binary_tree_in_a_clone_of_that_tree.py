# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(orig: TreeNode, cl: TreeNode) -> TreeNode:
            if orig is None:
                return None
            
            if orig is target:
                return cl
            
            r1 = dfs(orig.left, cl.left)
            r2 = dfs(orig.right, cl.right)
            
            return r1 or r2
        
        res = dfs(original, cloned)
        return res