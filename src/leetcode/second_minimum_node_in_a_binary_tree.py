# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if node is None:
                return None
            
            lv = dfs(node.left)
            rv = dfs(node.right)
            
            return get_min(lv, rv, node.val)
        
        def get_min(v1, v2, default_value):
            if v1 is None and v2 is None:
                return default_value
            elif v1 == root.val:
                return v2
            elif v2 == root.val:
                return v1
            
            return min(v1, v2)
        
        lmin = dfs(root.left)
        rmin = dfs(root.right)
        
        if lmin == rmin == root.val:
            return -1
        
        res = get_min(lmin, rmin, -1)
        return res