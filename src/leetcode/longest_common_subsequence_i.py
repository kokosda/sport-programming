class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        len_a, len_b = len(a), len(b)
        
        if len_a != len_b:
            return max(len_a, len_b)
        
        res = 0
        
        for i in range(len_a):
            if a[i] != b[i]:
                return len_a
        
        return -1