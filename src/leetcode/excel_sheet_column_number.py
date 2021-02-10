class Solution:
    def titleToNumber(self, s: str) -> int:
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        chars_dict = {}
        
        for i in range(len(chars)):
            chars_dict[chars[i]] = i
            
        base = 26
        res = 0
        s = s[::-1]
        
        for ch_i in range(len(s)):
            ch = s[ch_i]
            i = chars_dict[ch]
            res += (i + 1) * pow(base, ch_i)
        
        return res
    
"""
AB = 1*26^1 + 2*26^0 = 28
ZY = 26*26^1 + 25 * 26 ^ 0
"""