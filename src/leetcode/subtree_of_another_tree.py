# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        sl, tl = [], []
        
        def dfs(node, l_nodes):
            if node is None:
                return
            
            if node.left is None and node.right is None:
                l_nodes.append(f'{str(node.val)}L')
                return
            else:
                l_nodes.append(str(node.val))
            
            if node.left:
                dfs(node.left, l_nodes)
            else:
                l_nodes.append('n')
                
            if node.right:
                dfs(node.right, l_nodes)
            else:
                l_nodes.append('n')
            
        dfs(s, sl)
        dfs(t, tl)
        
        #print(sl, tl)
        
        ss = '-'.join(sl)
        ts = '-'.join(tl)
        
        res = ss.find(ts)
        
        if res > 0:
            if ss[res - 1] == '-':
                return True
            else:
                return False
        
        return res == 0