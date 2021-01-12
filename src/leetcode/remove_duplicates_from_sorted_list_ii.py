# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        current_node = head
        prev_node = None
        
        while current_node:
            if current_node.next and current_node.next.val == current_node.val:
                tmp_prev_node = current_node
                
                while current_node and current_node.val == tmp_prev_node.val:
                    current_node = current_node.next
                    
                if tmp_prev_node == head:
                    head = current_node
                else:
                    prev_node.next = current_node
                    prev_node = current_node
            else:
                prev_node = current_node
                current_node = current_node.next
        
        return head
    
"""
head: 1
dv: none

head: 1 -> 1 -> 1
dv: 1

[1,2,3,4,4,6]
[1,1,1,2,3,4,4,6]
[1,1,1,2,3,4,4,6,6,6]
[1,2,3,4,6]
[]
[2]
[2,2]
[1,2,3,3,4,4,5]
"""