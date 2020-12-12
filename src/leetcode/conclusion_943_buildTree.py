# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder == None or inorder == None:
            return None

        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        io_root_ind = inorder.index(root.val)
        io_left_len = io_root_ind
        io_right_len = len(preorder) - io_left_len - 1

        def go_down(preorder, inorder):
            if len(inorder) == 0:
                return None

            if len(inorder) == 1:
                return TreeNode(inorder[0])

            root = TreeNode(preorder[0])
            io_root_ind = inorder.index(root.val)
            io_left_len = io_root_ind
            io_right_len = len(preorder) - io_left_len - 1

            root.left = go_down(preorder[1:io_left_len + 1], inorder[:io_root_ind])
            root.right = go_down(preorder[io_left_len + 1:], inorder[io_root_ind + 1:])

            return root

        root.left = go_down(preorder[1:io_left_len + 1], inorder[:io_root_ind])
        root.right = go_down(preorder[io_left_len + 1:], inorder[io_root_ind + 1:])
        
        return root