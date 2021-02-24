# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, is_left: bool) -> int:
            if not node:
                return 0
            
            if not node.left and not node.right:
                if is_left:
                    return node.val
                
                return 0
            
            s1 = dfs(node.left, True)
            s2 = dfs(node.right, False)
            
            return s1 + s2
        
        res = dfs(root, False)
        return res