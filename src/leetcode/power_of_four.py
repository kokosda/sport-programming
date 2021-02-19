class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        
        MAX_BITS = 32
        i = 0
        bits = 0
        
        while i < MAX_BITS:
            if (n >> i) & 1:
                if i % 2 != 0:
                    return False
                
                bits += 1
                
                if bits > 1:
                    return False
            
            i += 1
            
        return True
    
"""
100
"""