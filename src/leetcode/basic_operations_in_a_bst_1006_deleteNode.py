# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        node, parent = self.find_node(root, key)
        
        if not node:
            return root
        
        if not node.left and not node.right:
            self.delete_source_node(node, parent, None, None)
            
            if node == root:
                return None
        else:
            replacement_node, replacement_parent = self.get_replacement(node, parent)
            self.delete_source_node(node, parent, replacement_node, replacement_parent)

        return root
    
    def find_node(self, root: TreeNode, key: int) -> TreeNode:
        node = root;
        parent = None
        
        while node and node.val != key:
            if node.val > key:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right
                
        return [node, parent]
    
    def get_replacement(self, sourceNode: TreeNode, sourceParent: TreeNode) -> TreeNode:
        node = sourceNode
        parent = sourceParent
        
        if not node.right:
            return [node.left, parent]
        
        parent = node
        node = node.right
        
        while True:
            if node.left:
                parent = node
                node = node.left
            else:
                break

        return [node, parent]
            
    def delete_source_node(self, sourceNode: TreeNode, sourceParent: TreeNode, targetNode: TreeNode, targetParent: TreeNode):
        if sourceParent:
            if sourceParent.left == sourceNode:
                sourceParent.left = targetNode
            else:
                sourceParent.right = targetNode
            
        if targetNode:
            if targetNode != sourceNode.left:
                targetNode.left = sourceNode.left
                
            if targetNode != sourceNode.right:
                targetNode.right = sourceNode.right
            
        if targetParent:
            if targetParent.left == targetNode:
                targetParent.left = None
            else:
                targetParent.right = None