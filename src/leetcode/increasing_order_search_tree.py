# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = [None, None]
        
        def dfs(node: TreeNode):
            if node is None:
                return
            
            if node.left is None and res[0] is None:
                res[0] = TreeNode(node.val)
                res[1] = res[0]
            else:
                dfs(node.left)

                res[1].right = TreeNode(node.val)
                res[1] = res[1].right
                
            dfs(node.right)
        
        dfs(root)
        
        return res[0]
            
"""
                19
         5               20
    3          17                 40
      4     14     18         30       50
          12  16   
          
12->14->16->
1.r=3
3.l=n
1.r=3.r=n=5
"""