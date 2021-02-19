class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split = s.split()
        
        if len(pattern) != len(split):
            return False
        
        d = {}
        p = {}
        
        for i, ch in enumerate(pattern):
            if not d.get(ch):
                if p.get(split[i]):
                    return False
                
                d[ch] = split[i]
                p[split[i]] = ch
            elif d[ch] != split[i]:
                return False

        return True