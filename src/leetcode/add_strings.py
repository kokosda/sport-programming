class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        
        while p1 >= 0 or p2 >= 0:
            x1 = num1[p1] if p1 >= 0 else 0
            x2 = num2[p2] if p2 >= 0 else 0
            
            tmp_sum = int(x1) + int(x2) + carry
            value = tmp_sum % 10
            carry = tmp_sum // 10
            res.append(value)
            
            p1 -= 1
            p2 -= 1
            
        if carry > 0:
            res.append(carry)
        
        return ''.join([str(i) for i in reversed(res)])
    
"""
"0"
"0"
"20"
"151"
"99"
"99"
"999"
"2"
"""