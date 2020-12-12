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
            
            if node.val == p.val or node.val == q.val:
                return parent

            l = go_down(node.left, node)
            r = go_down(node.right, node)
            print(l.val if l != None else None, r.val if r != None else None, parent.val if parent != None else None)
            
            if l != None and l == r:
                return l
            
        lwa = go_down(root, None)
        return lwa

"""
[8,5,0,9,3,null,1,null,null,2,19,null,null,null,null,4,null,7]
2
4
"""