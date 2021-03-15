# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        #todo 2nd option via list
        return res
    
    def findTarget_common(self, root: TreeNode, k: int) -> bool:
        def dfs(node: TreeNode, set_sum: set[int]) -> bool:
            if node is None:
                return
            
            if (k - node.val) in set_sum:
                return True
            
            set_sum.add(node.val)
            
            r1 = dfs(node.left, set_sum)
            r2 = dfs(node.right, set_sum)
            
            return r1 or r2
            
        res = dfs(root, set())
        return res
    
"""
[5,3,6,2,4,null,7]
9

[0,1,3,4,5,6,7,10]
9
"""