"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        
        def go_down(node, right, parent):
            if node == None:
                return
            
            if right != None:
                node.next = right                
            elif parent.next != None:
                node.next = parent.next.left
            
            go_down(node.left, node.right, node)
            go_down(node.right, None, node)
            
        go_down(root.left, root.right, root)
        go_down(root.right, None, root)
        
        return root