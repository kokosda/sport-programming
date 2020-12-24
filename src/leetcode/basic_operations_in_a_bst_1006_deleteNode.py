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
        
        node, node_parent = self.find_node(root, key)
        
        if not node:
            return root
        
        if not node.left and not node.right:
            self.replace_in_parent(node, node_parent, None)
        elif node.left and not node.right:
            self.replace_in_parent(node, node_parent, node.left)
        elif node.right and not node.left:
            self.replace_in_parent(node, node_parent, node.right)
        else:
            inorder_successor, inorder_successor_parent = self.get_inorder_successor(node.right, node)
            self.swap_nodes(node, node_parent, inorder_successor, inorder_successor_parent)
            self.replace_in_parent(node, inorder_successor_parent, None)
        
        return root
        
    def find_node(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        parent = None
        
        while node and node.val != val:
            parent = node
            
            if val < node.val:
                node = node.left
            else:
                node = node.right
                
        return [node, parent]
    
    def get_inorder_successor(self, root: TreeNode, parent: TreeNode) -> TreeNode:
        node = root
        
        while node.left:
            parent = node
            node = node.left
                
        return [node, parent]
    
    def swap_nodes(self, source: TreeNode, sourceParent: TreeNode, target: TreeNode, targetParent: TreeNode):
        if sourceParent:
            self.replace_in_parent(source, sourceParent, target)
        else:
            source.val = target.val
        
        target.left = source.left
        
        if source != targetParent:
            self.replace_in_parent(target, targetParent, None)
            target.right = source.right
    
    def replace_in_parent(self, node: TreeNode, parent: TreeNode, next_node: TreeNode):
        if parent.left == node:
            parent.left = next_node
        else:
            parent.right = next_node

"""
[20,9,30,6,11,25,40,4,7,10,null,21,27,33, 42,1,5,null,null,null,null,null,24,26,29]
"""