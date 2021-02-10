# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        d = set()
        it = head
        res = False
        
        while it:
            if it not in d:
                d.add(it)
                it = it.next
            else:
                res = True
                break
        
        return res