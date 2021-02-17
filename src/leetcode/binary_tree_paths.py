# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        
        s = str(root.val)
        res = []
        
        def dfs(node, res, s):
            if not node:
                return
            
            s += f'->{node.val}'
            
            if not node.left and not node.right:
                res.append(s)
            
            dfs(node.left, res, s)
            dfs(node.right, res, s)
            
        dfs(root.left, res, s)
        dfs(root.right, res, s)

        return res