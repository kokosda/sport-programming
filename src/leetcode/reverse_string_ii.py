class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        len_s = len(s)
        res = []
        i = 0
        
        while i < len_s:
            remaining_chrs = len_s - (i + 1)
            
            if remaining_chrs < k:
                res.append(s[i::][::-1])
                break
            elif k <= remaining_chrs < 2 * k:
                res.append(f'{s[i:i + k][::-1]}{s[i + k:]}')
                break
            
            res.append(f'{s[i:i + k][::-1]}{s[i + k:i + 2 * k]}')
            i += 2 * k
            
        return ''.join(res)