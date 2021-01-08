# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:        
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            
            if not node.left and not node.right:
                return node.val
            
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            print(f'n={node.val} l={left_val}, r={right_val}')
            
            max_s = max(node.val + left_val, node.val + right_val, node.val + left_val + right_val, node.val, left_val, right_val)
            
            return max_s
                
        res = dfs(root)
        return res
"""
state: current_val
value func: max sum
transition funcs: 
    1) node_i.val + l.val + r.val
    2) node_i.val + l.val
    3) node_i.val + r.val
    4) node_i.val
order: dfs
answer:
"""