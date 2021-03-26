# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        a = []
        
        def dfs(node: TreeNode):
            if node is None:
                return
            
            dfs(node.left)
            a.append(node.val)
            dfs(node.right)
            
        dfs(root)
        res = a[-1]
        
        for i in range(1, len(a)):
            res = min(res, a[i] - a[i - 1])
            
        return res