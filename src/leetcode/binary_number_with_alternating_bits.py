class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev_bit = n % 2
        n //= 2
        
        while n > 0:
            if n % 2 != prev_bit:
                prev_bit = n % 2
            else:
                return False
                
            n //= 2
            
        return True