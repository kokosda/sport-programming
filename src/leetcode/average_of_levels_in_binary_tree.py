# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        
        def dfs(node: TreeNode, res: List[float], level: int):
            if node is None:
                return 0
            
            if level > len(res):
                res.append([1, node.val])
            else:
                res[level - 1][0] += 1
                res[level - 1][1] += node.val
                
            dfs(node.left, res, level + 1)
            dfs(node.right, res, level + 1)
            
        dfs(root, res, 1)
        
        return [i[1] / i[0] for i in res]
    
"""
                   20
            10             11
        1       3      9         7
     8     2  6   5  0   4     5   12
     
(0 + 2 + 4 + 6) / 4
(0 + 2) / 2 = 1
(4 + 6) / 2 = 5
(1 + 5)/ 2 = 3
2/4 + 4/4 + 6/4 = 1/2 + 1 + 3/2 = 3
"""