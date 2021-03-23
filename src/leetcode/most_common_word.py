class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punc = set(" !?',;.")
        banned = set(banned)
        w = ''
        fi = None
        li = 0
        d = dict()
        
        for i in range(len(paragraph)):
            ch = paragraph[i]
            
            if ch in punc:
                if fi is not None and li - fi >= 0:
                    Solution._update_word(paragraph, banned, d, fi, i)                        
                    fi = None
                continue
                
            if fi is None:
                fi = i
                
            li = i
        else:
            Solution._update_word(paragraph, banned, d, fi, i + 1)
            
        max_k = None
        max_count = 0
        print(d)
        
        for k in d:
            if d[k] > max_count:
                max_k = k
                max_count = d[k]
            
        return max_k
    
    def _update_word(paragraph, banned, d, fi, i):
        w = paragraph[fi:i].lower()

        if w not in banned:
            d[w] = d.get(w, 0) + 1

"""
"Bob hit a ball, the hit BALL flew far after it was hit."
["hit"]
"""