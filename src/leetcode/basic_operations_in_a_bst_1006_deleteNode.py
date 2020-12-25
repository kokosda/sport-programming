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
        
        if node == root:
            inorder_successor, inorder_successor_parent = self.get_inorder_successor(node.right, node)
            
            if inorder_successor:
                if inorder_successor == root.right:
                    root_left = root.left
                    root = inorder_successor
                    root.left = root_left
                else:
                    root.val = inorder_successor.val

                    if inorder_successor.right:
                        inorder_successor_parent.left = inorder_successor.right
                    else:
                        inorder_successor_parent.left = None
            else:
                root = root.left

            return root
        
        if not node.left and not node.right:
            self.replace_child_in_parent(node_parent, node, None)
        else:
            while True:
                inorder_successor, inorder_successor_parent = self.get_inorder_successor(node.right, node)
                self.swap_nodes(node, node_parent, inorder_successor, inorder_successor_parent)
                node = inorder_successor
                
                if not inorder_successor.right:
                    break
                
            self.replace_child_in_parent(inorder_successor_parent, inorder_successor, None)
        
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
    
    def swap_nodes(self, source: TreeNode, sourceParent: TreeNode, target: TreeNode, targetParent: TreeNode):
        source.val, target.val = target.val, source.val
    
    def replace_child_in_parent(self, parent: TreeNode, source: TreeNode, target: TreeNode):
        if parent.left == source:
            parent.left = target
        else:
            parent.right = target

"""
[20,9,30,6,11,25,40,4,7,10,null,21,27,33, 42,1,5,null,null,null,null,null,24,26,29]

[2,0,33,null,1,25,40,null,null,11,31,34,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,35,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41] 
33 -- input
[2,0,33,null,1,25,40,null,null,11,31,34,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,35,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41] -- wrong
[2,0,34,null,1,25,40,null,null,11,31,35,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,null,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,38,null,41] -- right
"""