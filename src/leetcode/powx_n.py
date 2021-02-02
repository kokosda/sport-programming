class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if x == 0:
            return 0
        
        if n < 0:
            x = 1 / x
            n = -n
            
            if n == 1:
                return x
        
        t = 2
        x0 = x
        sum = 0
        
        while t > 0:
            t = 2
            x = x0
            x = x * x
            
            while (t * 2) <= n:
                x = x * x
                t *= 2
                print(t)

            n -= t
            sum += x
            
        return x
    
"""
logxS = n
S = x ^ n

"""
s = Solution()
s.myPow(0.00001, 2147483647)