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
        elif not node.right and not self.has_children(node.left):
            self.swap_nodes(node, node.left)
            self.delete_child(node, node.left)
        elif not node.left and not self.has_children(node.right):
            self.swap_nodes(node, node.right)
            self.delete_child(node, node.right)
        else:
            while True:
                inorder_successor, inorder_successor_parent = None, None
                
                if node.right:
                    inorder_successor, inorder_successor_parent = self.get_inorder_successor(node.right, node)
                else:
                    if not self.has_children(node):
                        break

                    node_parent.right = node.left
                    return root
                    
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

"""
[20,9,30,6,11,25,40,4,7,10,null,21,27,33, 42,1,5,null,null,null,null,null,24,26,29]

[2,0,33,null,1,25,40,null,null,11,31,34,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,35,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41] 
33 -- input
[2,0,33,null,1,25,40,null,null,11,31,34,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,35,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41] -- wrong
[2,0,34,null,1,25,40,null,null,11,31,35,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,null,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,38,null,41] -- right

[41,12,48,5,14,42,49,1,10,13,16,null,47,null,null,0,3,9,11,null,null,15,35,44,null,null,null,2,4,7,null,null,null,null,null,27,39,43,46,null,null,null,null,6,8,19,28,37,40,null,null,45,null,null,null,null,null,18,25,null,31,36,38,null,null,null,null,17,null,23,26,29,32,null,null,null,null,null,null,22,24,null,null,null,30,null,33,21,null,null,null,null,null,null,34,20]
22 -- input

[41,12,48,5,14,42,49,1,10,13,16,null,47,null,null,0,3,9,11,null,null,15,35,44,null,null,null,2,4,7,null,null,null,null,null,27,39,43,46,null,null,null,null,6,8,19,28,37,40,null,null,45,null,null,null,null,null,18,25,null,31,36,38,null,null,null,null,17,null,23,26,29,32,null,null,null,null,null,null,21,24,null,null,null,30,null,33,20,null,null,null,null,null,null,34] -- right
"""