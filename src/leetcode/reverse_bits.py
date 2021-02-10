class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        
        while n > 0:
            res = res * 2 + n % 2
            n = n // 2
            i += 1
            
        return res << (32 - i)
    
    def reverseBitsSimple(self, n: int) -> int:
        s = ''
        
        while n > 0:
            i = n % 2
            s += str(i)
            n = n // 2
            
        s = '0' * (32 - len(s)) + s[::-1]
        res = 0

        for i in range(len(s)):
            if s[i] == '0':
                continue
            
            res += pow(2, i)
            
        return res
    
"""
10100
(((1*2 + 0)*2 + 1)*2 + 0)*2 + 0

00101

20
10100 - s, 32 - s
00101[0]
"""