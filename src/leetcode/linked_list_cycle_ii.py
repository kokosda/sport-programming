# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        x, y = 0, 0
        slow, fast = head, head
        
        while True:
            
            if slow.next:
                slow = slow.next
                x += 1
            else:
                return None
            
            if fast.next and fast.next.next:
                fast = fast.next.next
                y += 2
                
            if slow == fast:
                break
        
        print(x, y)
        return None