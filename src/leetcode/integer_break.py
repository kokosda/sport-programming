class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        
        r = n % 3
        m = n // 3
        
        if r <= 1:
            m -= 1
            r = n - 3 * m

        result = r * 3 ** m
        return result
    
"""
20: 10 * 10 = 100
20: 2 * 3 * 3 * 3 * 3 * 3 * 3
20: 1 * 3 * 3 * 3 * 3 * 3 * 4

20 // 3 = 6
"""