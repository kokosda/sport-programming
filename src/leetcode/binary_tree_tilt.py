# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> (int, int):
            if node is None:
                return (0, 0)
            
            if node.left is None and node.right is None:
                return (0, node.val)
            
            diff_l, sum_l = dfs(node.left)
            diff_r, sum_r = dfs(node.right)
            
            return (diff_l + diff_r + abs(sum_l - sum_r), sum_l + sum_r + node.val)
        
        res = dfs(root)
        return res[0]