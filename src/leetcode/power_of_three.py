class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 3 == 0:
            n //= 3
            
        return n == 1
    
    def isPowerOfThree2(self, n: int) -> bool:
        if n <= 0:
            return False
        
        x = 1
        
        while x < n:
            x *= 3
            
        return x == n
            
        
"""
000001
000011
000101
011011
101101

27 / 2 = 13(1)
13 / 2 = 6(1)
6 / 2 = 3(0)
3 / 2 = 1(1)
1 / 2 = 0(1)

81 / 2 = 40 (1)
40 / 2 = 20 (0)
20 / 2 = 10 (0)
10 / 2 = 5 (1)
5 / 2 = 2 (1)
2 / 2 = 1 (0)
1 / 2 = 1
"""