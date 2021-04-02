class Solution:
    A_LOWER_CODE = ord('a')
    
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        res = set()
        
        for i in range(len(A)):
            key_str = self._to_full_key_str(A[i])
            
            if key_str not in res:
                res.add(key_str)
                
        return len(res)
    
    def _to_full_key_str(self, s: str) -> str:
        even_k_s = self._to_key_str(s[::2])
        odd_k_s = self._to_key_str(s[1::2])
        return f'{even_k_s}-{odd_k_s}'
    
    def _to_key_str(self, s: str) -> str:
        res = [0] * 26
        
        for ch in s:
            res[ord(ch) - Solution.A_LOWER_CODE] += 1

        return '-'.join([str(i) for i in res])
    
"""
zzxy
zzyx
----
1. zyxz
1. zxyz

xyzz
zzxy

abc
acb
"""