class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        i = 0
        
        while True:                
            i += 1
            
            if i <= n:
                n -= i
                count += 1
            else:
                break
                
        return count
    
    def arrangeCoins_equation(self, n: int) -> int:
        a_sum = n * ((n + 1) / 2)
        res = (-1 + sqrt(1 + 8 * a_sum)) / 2
        print(res, a_sum)
        return int(res) - n
    
"""
36 = x * (x + 1) / 2 => (x^2 + x) / 2 = 36 => x^2 + x - 72 = 0 => d = -b/2 +- sqrt((b/2)**2 - a*c) => -1/2 +- sqrt(1/4 + 2S)

S = 8 * ((8 + 1) / 2) = 36

1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36

(x * (x + 1)) / 2 = S
(x^2 + x) / 2 - S = 0
x^2 + x - 2S = 0
-4*1*-2S=8*S
x = (-1 + sqrt(1 + 8S)) / 2

16^2 + 16 - 2*36 = 0
"""
