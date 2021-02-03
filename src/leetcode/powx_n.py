class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        if n < 0:
            x = 1 / x
            n = -n
        
        x0 = x
        p = 1
        
        while n > 0:
            t = 1
            x = x0
            
            while (t * 2) <= n:
                x = x * x
                t *= 2
            
            n -= t
            
            if n >= 0:
                p *= x
            else:
                for i in range(abs(n)):
                    p *= x0
            
        return p
    
"""
3.02
-7
9.34
4
2
-5
0.00001
2147483647
2.00000
10
"""