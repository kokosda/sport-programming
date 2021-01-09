# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_s: int) -> int:
            if not node:
                return max_s
            
            if not node.left and not node.right:
                return max(node.val, max_s)
            
            max_s = max(dfs(node.left, max_s), dfs(node.right, max_s))
            left_val = node.left.val if node.left else min(max_s, 0)
            right_val = node.right.val if node.right else min(max_s, 0)
            max_s = max(max_s, node.val + left_val + right_val, node.val, left_val, right_val)
            node.val = max(node.val + left_val, node.val + right_val)
            print(f'n={node.val} l={left_val}, r={right_val}')
            
            return max(node.val, max_s)
                
        res = dfs(root, root.val)
        return res
    
"""
dynamic state: node (value)
dynamic value func: path of max sum
dynamic initial states: leaf values
dynamic transition funcs: 
    1) node_i.val + l.val + r.val
    2) node_i.val + l.val
    3) node_i.val + r.val
    4) node_i.val
order of calculation: dfs
answer to the original problem: 

[1,2,3]
[-10,9,20,null,null,15,7]
[-10,90,20,null,null,15,7]
[-1,-2]
[1,-2,3]
[-1,5,null,4,null,null,2,-4]
"""