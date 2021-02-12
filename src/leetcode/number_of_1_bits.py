class Solution:
    def hammingWeight(self, n: int) -> int:
        max_bits = 32
        bits = 0
        i = 0
        
        while i <= max_bits:            
            if (n >> i) & 1:
                bits += 1

            i += 1
            
        return bits
            
"""
11 - 1011
"""