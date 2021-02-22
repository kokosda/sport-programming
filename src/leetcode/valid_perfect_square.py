class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num // 2
        
        while (l + 1) < r:
            m = (l + r) // 2
            
            if m * m <= num:
                l = m
            else:
                r = m
                
        return l * l == num
    
"""
100
1
2
3
16
17
256
4

l = 1
r = 50

m = 25
r = 25

m = 12
r = 12

m = 6
r = 12

l = 6 + 12 = 9
r = 12

l = 9 + 12 = 21 // 2 = 10
r = 12

l = 10
r = 11


"""