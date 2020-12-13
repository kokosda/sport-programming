# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def go_down(node, parent):
            if node == None:
                return None

            l = go_down(node.left, node)
            r = go_down(node.right, node)
            
            if node.val == p.val or node.val == q.val:
                if node == l or node == r:
                    return node

                return parent
            
            if l == r and l == node:
                return l
            
            if l == node or r == node:
                return parent
            
            if l != None:                    
                return l
            
            if r != None:
                return r
            
            return None
            
        lwa = go_down(root, None)
        return lwa

"""
[8,5,0,9,3,null,1,null,null,2,19,null,null,null,null,4,null,7]
2
4
"""