class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:        
        res = []
        
        for h in range(0, 12):
            for m in range(0, 60):
                bits_h = bin(h).count('1')
                bits_m = bin(m).count('1')
                
                if bits_h + bits_m == num:
                    res.append(f'{h}:{m:02d}')
                    
        return res
                
"""
0011 - 3
011001 - 25

1111

111001

n
"""