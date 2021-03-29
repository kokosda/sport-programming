# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast_p = head
        slow_p = head
        
        while fast_p is not None and fast_p.next is not None:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            
        return slow_p