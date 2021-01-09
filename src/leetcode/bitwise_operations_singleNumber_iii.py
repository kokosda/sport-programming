import math

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_res = 0
        
        for i in nums:
            xor_res ^= i
            
        inverted = self.invert_bits(xor_res)
        print(xor_res)
        res1 = xor_res - inverted
        res2 = xor_res ^ res1
        
        candidates = [0, 0, 0, 0]
        i = 0
        
        while xor_res > 0:
            bit = (xor_res >> 1) & 1
            
            if bit == 1:
                candidates[0] |= (1 << i)
                candidates[1] &= ~(1 << i)
                candidates[2] &= ~(1 << i)
                candidates[3] |= (1 << i)
            else:
                candidates[0] |= (1 << i)
                candidates[1] |= (1 << i)
                candidates[2] &= ~(1 << i)
                candidates[3] &= ~(1 << i)
                
            xor_res >>= 1
            i += 1
        print(candidates)
        return [res1, res2]
    
    def invert_bits(sef, num):  
        x = int(math.log2(num)) + 1

        for i in range(x):  
            num = (num ^ (1 << i))  

        return num
    
"""
[1,2,1,3,2,5]
101 - 5
011 - 3
110 - 6

110

000
001
111
110
110
001

110 - 001 = 101

00011 - 3
10001 - 17
10010 - 18
01101 - 13
"""