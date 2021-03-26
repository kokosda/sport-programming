class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 }
        res = 0
        
        for i in range(L, R + 1):
            n = i
            bits = 0
            
            while n > 0:
                bits += n & 1
                n >>= 1
                
            if bits in primes:
                res += 1
        
        return res
    
    def _get_primes() -> set[int]:
        res = { i for i in range(2, 32) }
        
        for i in range(2, 32):
            for j in range(2, i):
                if i != j and i % j is 0 and i in res:
                    res.remove(i)
                    
        return res
                    
    
    def countPrimeSetBits_remainder(self, L: int, R: int) -> int:
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
    
"""
010011001
001001100
000000001
"""