# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        leveled_arrays = self.get_leveled_array(root)

        for array in leveled_arrays:
            i, j = 0, len(array) - 1

            while i < j:
                if array[i] != array[j]:
                    return False
                
                i += 1
                j -= 1
                
        return True

    def get_leveled_array(self, root: TreeNode) -> bool:
        q = [[root, 1]]
        qi = 0
        r = []

        while qi < len(q):
            cr, depth = q[qi]
            v = cr.val if cr != None else None
            
            if len(r) < depth:
                r.append([v])
            else:
                r[depth - 1].append(v)
                
            if cr == None:
                qi += 1
                continue
            
            if cr.left != None:
                q.append([cr.left, depth + 1])
            else:
                q.append([None, depth + 1])
                
            if cr.right != None:
                q.append([cr.right, depth + 1])
            else:
                q.append([None, depth + 1])
                
            qi += 1
                
        return r