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

        def go_down(inorder, postorder, root, flag):
            if len(inorder) == 0:
                return

            if len(inorder) == 1:
                if flag == 0:
                    root.left = TreeNode(inorder[0])
                else:
                    root.right = TreeNode(inorder[0])

                return

            root_ind = inorder.index(root.val)
        
        go_down(inorder[0:root_ind], postorder[0:root_ind], root, 0)
        go_down(inorder[root_ind + 1:], postorder[root_ind:-1], root, 1)
        
        return root
