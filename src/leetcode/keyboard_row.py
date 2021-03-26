class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set('qwertyuiop' + 'qwertyuiop'.upper())
        row2 = set('asdfghjkl' + 'asdfghjkl'.upper())
        row3 = set('zxcvbnm' + 'zxcvbnm'.upper())
        
        res = []
        
        for w in words:
            w_set = set(w)
            
            if len(w_set - row1) == 0 or len(w_set - row2) == 0 or len(w_set - row3) == 0:
                res.append(w)
                
        return res