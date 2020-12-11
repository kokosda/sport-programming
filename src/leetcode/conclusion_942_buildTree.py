# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder == None or postorder == None:
            return None

        if len(inorder) == 0 or len(postorder) == 0:
            return None

        root = TreeNode(postorder[-1])
        root_ind = inorder.index(root.val)

        def go_down(inorder, postorder):
            print("inorder ", inorder, " posorder", postorder)
            if len(inorder) == 0:
                return None

            if len(inorder) == 1:
                return TreeNode(inorder[0])

            root = TreeNode(postorder[-1])
            root_ind = inorder.index(root.val)

            root.left = go_down(inorder[0:root_ind], postorder[0:root_ind])
            root.right = go_down(inorder[root_ind + 1:], postorder[root_ind:-1])
            
            return root

        root.left = go_down(inorder[0:root_ind], postorder[0:root_ind])
        root.right = go_down(inorder[root_ind + 1:], postorder[root_ind:-1])

        return root
"""
inorder: [9,5,3,2,19,8,0,1]
postord: [9,2,19,3,5,1,0,8]

inorder_l1: [9,5,3,2,19] root 8
postord_l1: [9,2,19,3,5] root 8

inorder_l2: [9] root 5
postord_l2: [9] root 5
inorder_r2: [3,2,19] root 5
postord_r2: [2,19,3] root 5

inorder_l3: [] root 3
postord_l3: [] root 3
inorder_r3: [2,19] root 3
postord_r3: [2,19] root 3

inorder_l4: [2] (root 19)
postord_l4: [2] (root 19)
inorder_r4: [] root 19
postord_r4: [] root 19

inorder_r1: [0,1] root 8
postord_r1: [1,0] root 8
"""
