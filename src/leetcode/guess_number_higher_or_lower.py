# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n + 1
        
        while l < r:
            m = (l + r) // 2
            g = guess(m)
            
            if g == 0:
                return m
            elif g == 1:
                l = m
            else:
                r = m
                
        return l
    
"""
10
6
10
1
10
10
10
5
100
2
"""