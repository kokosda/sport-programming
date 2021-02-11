class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        if n == 3:
            return 1
        if n == 4:
            return 2
        
        res = 2
        i = 3
        
        while i < n - 1:
            i += 2
            
            if not i % 3:
                continue
                
            divisible = False
            
            for j in range(2, int(math.sqrt(i)) + 1):
                if not i % j:
                    divisible = True
                    break
                    
            if not divisible:
                res += 1
            
        return res
"""
'0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20'
         ^   ^   ^   ^     ^     ^     ^     ^
             ^     ^       ^        ^        ^
                     ^              ^              ^

i: 5
"""