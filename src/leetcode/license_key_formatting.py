class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        m = [''] * len(S)
        group = K
        i = len(S) - 1
        
        while i >= 0:
            while i >= 0 and S[i] == '-':
                i -= 1
                
            if i < 0:
                break
                
            if group > 0:
                m[i] = S[i]
                group -= 1
            else:
                m[i] = f'{S[i]}-'
                group = K-1
                
            i -= 1

        res = ''.join(m).upper()
        return res
    
"""
"---3g-ff---"
2
"2-5g-3-J"
2
"5F3Z-2e-9-w"
4
"5F3Z-2e-9-w"
40
"""