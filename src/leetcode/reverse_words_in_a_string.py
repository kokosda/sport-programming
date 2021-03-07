class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        k = 0
        
        for i in range(len(s)):
            if s[i] == ' ':
                res.append(s[k:i][::-1])
                k = i + 1
        else:
            res.append(s[k:i + 1][::-1])
                
        return ' '.join(res)