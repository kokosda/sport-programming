class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        ranges = [bin(i).count('1') for i in range(L, R + 1)]
        res = 0
        
        for el in ranges:
            if self._is_prime(el):
                res += 1
                
        return res
            
    def _is_prime(self, num: int) -> bool:
        if num is 1:
            return False
        
        for i in range(2, num):
            if num % i is 0:
                return False
            
        return True