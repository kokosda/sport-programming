# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        
        prev1, it1, it2 = None, head, head
        
        while it2 != None and it2.next != None:
            it2 = it2.next.next
            
            tmp = it1
            it1 = it1.next
            tmp.next = prev1
            prev1 = tmp
            
        if it2 != None:
            it1 = it1.next
            
        while prev1 != None and it1 != None:
            if prev1.val != it1.val:
                return False
            
            prev1 = prev1.next
            it1 = it1.next
            
        return True

"""
6-1-3-2-5

3-4-1-5-1-4-3

tmp: 3
tmp.next: None
it: 4

[1]
[]
[2,2]
[4,1,5,1,4]
[4,1,1,4]
"""