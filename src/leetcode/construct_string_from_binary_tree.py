# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:        
        def dfs(node: TreeNode):
            if node is None:
                return ''
            
            if node.left is None and node.right is None:
                return str(node.val)
            
            lr = dfs(node.left)
            rr = dfs(node.right)
            
            if node.right is None:
                return f'{node.val}({lr})'                
            else:
                return f'{node.val}({lr})({rr})'
            
        return dfs(t)