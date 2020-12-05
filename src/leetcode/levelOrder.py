# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        q = [[root, 0]]
        qi = 0
        r = []
        
        while qi < len(q):
            cr, depth = q[qi]
            
            if len(r) < depth + 1:
                r.append([cr.val])
            else:
                r[depth].append(cr.val)
            
            if cr.left != None:
                q.append([cr.left, depth + 1])
            
            if cr.right != None:
                q.append([cr.right, depth + 1])
                
            qi += 1
            
        return r
    
#[8,5,0,9,3,null,1,null,null,2,null]
#cr: 2
#depth: 3
#r: [[8],[5,0],[9,3,1]]
#q: [[8, 0],[5,1],[0,1],[9,2],[3,2],[1,2],[2,3]]
#qi: 7