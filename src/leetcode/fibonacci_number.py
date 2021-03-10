class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        prev, cur = 0, 1
        i = 2
            
        while i <= n:
            prev, cur = cur, prev + cur
            i += 1
            
        return cur