# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        it1, it2 = head, head
        
        while it1:            
            it1 = it1.next
            
            if it2.next:
                if it2.next.next:
                    it2 = it2.next.next
                else:
                    return False
                
            if it1 and it2 and it1 == it2 and it2.next:
                return True
                
        return False
    
    def hasCycleViaSet(self, head: ListNode) -> bool:
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