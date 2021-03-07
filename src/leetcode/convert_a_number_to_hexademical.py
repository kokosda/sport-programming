class Solution:
    def toHex(self, num: int) -> str:
        letters = string.digits + string.ascii_lowercase
        l = []

        while True:
            m = num % 16
            num //= 16
            l.append(m)
            
            if num == 0 or num == -1:
                break

        res = ''.join([letters[l[i]] for i in range(len(l) - 1, -1, -1)])
        
        if num < 0:
            res = res.rjust(8, 'f')
        
        return res
    
"""
n = (n // b) * b + (n % b)
-2 = (-2 // 16) * 16 + (-2 % 16) = -1 * 16 + 14 = -2
"""