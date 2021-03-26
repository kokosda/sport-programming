# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Stat:
    def __init__(self):
        self.count = 0
        self.modes = []
        
class Solution:
    #following is incorrect and works only with conitguous duplicates
	#to make it work properly implement in-order traversal
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        def dfs(node: TreeNode, stat: Stat) -> int:
            if not node:
                return 0
            
            cur_count = 1
            
            lc = dfs(node.left, stat)
            rc = dfs(node.right, stat)
            
            if node.left and node.left.val == node.val:
                cur_count += lc
                
            if node.right and node.right.val == node.val:
                cur_count += rc
            
            if cur_count == stat.count:
                stat.modes.append(node.val)
            elif cur_count > stat.count:
                stat.count = cur_count
                stat.modes = [node.val]
                
            return cur_count
            
        stat = Stat()
        dfs(root, stat)
        
        return stat.modes
    
    def findMode_dictionary(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        d = dict()
        
        def dfs(node: TreeNode, d):
            if node is None:
                return
            
            dfs(node.left, d)
            dfs(node.right, d)
            
            d[node.val] = d.get(node.val, 0) + 1
            
        dfs(root, d)
        
        res = []
        max_el = 0
        
        for _, v in d.items():
            max_el = max(max_el, v)
                
        for k, v in d.items():
            if v == max_el:
                res.append(k)
            
        return res
    
"""
                      10
                2            15
             2     2       15 
             
             
             
                      10
                2            15
             1     2       15  15
           1     2   3   15
         1      2     3
                     3 3
                     
[1,null,2,2,2,2]
[10,2,15,1,2,15,15,1,null,2,3,15,null,null,null,1,null,2,null,null,3,null,null,null,null,null,null,3,3]
[10,2,15,1,2,15,15,1,null,2,3,15,null,null,null,1,null,2,null,null,3,null,null,null,null,2,null,3,3]
"""