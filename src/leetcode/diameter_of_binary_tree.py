# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> (int, int, int):
            if node is None:
                return (0, 0, 0)
            
            count_left = dfs(node.left)
            count_right = dfs(node.right)
            
            info = (1 + max(count_left[0], count_left[1]), \
                    1 + max(count_right[0], count_right[1]), \
                    max(1 + max(count_left[0], count_left[1]) + max(count_right[0], count_right[1]), \
                        count_left[2], count_right[2]))
            #print(res2, node.val)
            return info
        
        res = dfs(root)
        return res[2] - 1
"""
                7
          2           1
      9      3
    5  12      4
      13      6
      
[7,2,1,9,3,null,null,5,12,null,4,null,null,13,null,6]
longest: [13-12-9-2-3-4-6]
"""