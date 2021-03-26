class Solution:
    def toLowerCase(self, str: str) -> str:
        res = []
        cap_a_ord = ord('A')
        cap_z_ord = ord('Z')
        low_a_ord = ord('a')
        diff = cap_a_ord - low_a_ord
        
        for ch in str:
            ch_ord = ord(ch)
            
            if cap_a_ord <= ch_ord <= cap_z_ord:
                ch_ord -= diff
                res.append(chr(ch_ord))
            else:
                res.append(ch)
                
        return ''.join(res)