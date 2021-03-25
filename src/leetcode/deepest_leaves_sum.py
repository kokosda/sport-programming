# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        level_sum = [0, root.val]
        
        def dfs(node: TreeNode, level: int):
            if node is None:
                return
            
            if node.left is None and node.right is None:
                if level_sum[0] == level:
                    level_sum[1] += node.val
                elif level_sum[0] < level:
                    level_sum[1] = node.val
                    level_sum[0] = level
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
        dfs(root, 0)
        
        return level_sum[1]