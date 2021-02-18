class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        v = {}
        
        for ch in s:
            if not v.get(ch):
                v[ch] = 1
            else:
                v[ch] += 1
                
        for ch in t:
            if v.get(ch):
                v[ch] -= 1
                
                if v[ch] < 0:
                    return False
            else:
                return False
            
        return True