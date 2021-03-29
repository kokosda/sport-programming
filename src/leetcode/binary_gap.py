class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        prev_bit = -1
        i = 0
        cur_bit = -1
        
        while n > 0:
            if n & 1 is 1:
                prev_bit = cur_bit
                cur_bit = i
                #print(cur_bit, prev_bit)
                if prev_bit > -1:
                    res = max(res, cur_bit - prev_bit)
                
            n >>= 1
            i += 1
            
        return res