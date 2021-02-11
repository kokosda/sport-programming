class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:        
        d = {}
        values = set()
        
        for i in range(len(s)):
            if not d.get(s[i]):
                if d.get(t[i]) and d[t[i]] == t[i] or t[i] in values:
                    return False
                
                values.add(t[i])
                d[s[i]] = t[i]
                continue
                
            if d[s[i]] != t[i]:
                return False
            
        return True
            
"""
"db"
"bb"
"paper"
"title"
"er"
"le"
"bd"
"bb"
"badc"
"baba"
"foo"
"bar"
"m"
"n"
"m"
"m"
"egg"
"add"
"""