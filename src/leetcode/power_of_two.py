class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: 
            return False
        
        max_bits = 32        
        bits, i = 0, 0
        
        while i < max_bits:
            if (n >> i) & 1:
                bits += 1
                
                if bits > 1:
                    return False
                
            i += 1
            
        return bits == 1
            
"""
17 - 10001
1
2
16
-2147483648
17
3468684
-4
-6
0
"""