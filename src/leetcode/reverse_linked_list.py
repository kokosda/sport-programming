# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        def go(node: ListNode, prevNode: ListNode):
            if not node:
                return prevNode
            
            tmp = node
            node = node.next
            tmp.next = prevNode
            
            return go(node, tmp)
        
        head = go(head, None)        
        return head
    
    def reverseListIterative(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        prev, it = None, head
        
        while it:
            tmp = it
            it = it.next
            tmp.next = prev
            prev = tmp
            
        head = prev
        return head
    
"""
1->2->3->NULL
1-> : 1->NULL
2-> : 2->1

p: none
it: 1

tmp: 1 (->2)
it: 2
tmp.next: none
prev: 1

tmp: 2 (->3)
it: 3
tmp.next: 1
prev: 2
"""