# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            
            s1 = 0
            s2 = 0
            
            if node.val >= low and node.val <= high:
                s1 = dfs(node.left) + node.val
                s2 = dfs(node.right)
            elif node.val < low:
                s1 = dfs(node.right)
            elif node.val > high:
                s2 = dfs(node.left)
                
            return s1 + s2
            
        return dfs(root)
            
"""
[7,14]
5
"""