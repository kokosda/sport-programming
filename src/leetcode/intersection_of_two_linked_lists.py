# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        if headA == headB:
            return headA
        
        def get_length(node: ListNode) -> int:
            res = 0
            
            while node:
                node = node.next
                res += 1
                
            return res
        
        def skip_nodes(node: ListNode, count: int):
            while count > 0:
                node = node.next
                count -= 1
                
            return node
        
        it_a, it_b = headA, headB
        len_a, len_b = get_length(headA), get_length(headB)
        
        if len_a > len_b:
            it_a = skip_nodes(it_a, len_a - len_b)
        elif len_a < len_b:
            it_b = skip_nodes(it_b, len_b - len_a)
            
        
        while it_a and it_b:
            if it_a == it_b:
                return it_a
            
            it_a = it_a.next
            it_b = it_b.next
            
        return None
    
"""
[4,1,  8,4,5]
[5,6,1,8,4,5]
"""