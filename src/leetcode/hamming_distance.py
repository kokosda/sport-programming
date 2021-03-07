class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        i = 0
            
        while i < 32:
            bit_x = (x >> i) & 1
            bit_y = (y >> i) & 1
            
            if bit_x != bit_y:
                res += 1
                
            i += 1
                
        return res