# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        
        prev, cur = None, head
        
        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                    cur = cur.next
                else:
                    head = cur.next
                    cur = cur.next
                
                continue
            
            prev = cur
            cur = cur.next
            
        return head
    
"""
[1,2,3,4,5,6]
           ^
p: none
c: 1

1 == 6
p: 1
c: 2

...
p: 5
c: 6

6 == 6
5.next: 6.next -> None

[6,2,3,4,5,6]
           ^
p: none
c: 6

6 == 6
head: 2
p: 6
c: 2

2 == 6
p: 2
c: 3


"""