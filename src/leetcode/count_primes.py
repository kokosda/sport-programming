class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        res = 1
        m = [True] * n
        
        for i in range(4, n, 2):
            m[i] = False
        
        for i in range(3, n, 2):
            if m[i]:
                res += 1
                
                for j in range(i * i, n, i):
                    m[j] = False
            
        return res
    
"""
'0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22'
         ^   ^   ^   ^     ^     ^     ^     ^     ^     ^
             ^     ^       ^        ^        ^        ^
                     ^              ^              ^
                                 ^                    ^
                                                         ^
i: 5

221: 13 * 17
"""