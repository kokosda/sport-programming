class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        prev_ch = ''
        
        for ch in s:
            if ch != ' ' and (prev_ch == '' or prev_ch == ' '):
                count += 1
                
            prev_ch = ch
            
        return count
    
"""
"Hello, my name is John"
"Hello"
"Hello Hello"
" Hello"
" Hello "
" H "
"H"
"H "
""
"love live! mu'sic forever"
"love live!  mu'sic  forever"
"         "
"""