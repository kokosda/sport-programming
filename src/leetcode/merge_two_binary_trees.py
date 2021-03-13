# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        
        def dfs(node1: TreeNode, node2: TreeNode):           
            node1.val += node2.val
                
            if node1.left is not None and node2.left is not None:
                dfs(node1.left, node2.left)
            
            if node1.left is None and node2.left is not None:
                node1.left = node2.left
                
            if node1.right is not None and node2.right is not None:
                dfs(node1.right, node2.right)
                
            if node1.right is None and node2.right is not None:
                node1.right = node2.right
                
        dfs(root1, root2)
        
        return root1