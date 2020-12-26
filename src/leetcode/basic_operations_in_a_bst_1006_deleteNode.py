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
        
        if not self.has_children(node):
            if node == root:
                return None
            
            self.delete_child(node_parent, node)
        elif not node.right and node.left:
            if node == root:
                return node.left
            
            self.set_child(node_parent, node, node.left)
        else:
            while True:
                inorder_successor, inorder_successor_parent = self.get_inorder_successor(node.right, node)
                self.swap_nodes(node, inorder_successor)
                node = inorder_successor
                node_parent = inorder_successor_parent
                
                if not inorder_successor.right:
                    break
                
            self.delete_child(node_parent, node)
        
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
        if not root:
            return [root, parent]
        
        node = root
        
        while node.left:
            parent = node
            node = node.left
                
        return [node, parent]
    
    def swap_nodes(self, source: TreeNode, target: TreeNode):
        source.val, target.val = target.val, source.val
        
    def has_children(self, node: TreeNode) -> bool:
        if not node:
            return False
        
        return node.left or node.right
    
    def delete_child(self, parent: TreeNode, source: TreeNode):
        if parent.left == source:
            parent.left = None
        else:
            parent.right = None
            
    def set_child(self, parent: TreeNode, source: TreeNode, node: TreeNode):
        if parent.left == source:
            parent.left = node
        else:
            parent.right = node