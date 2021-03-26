class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:                
        store = dict()
        min_len_word = 0
        
        for ch in licensePlate:
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                store[ch.lower()] = store.get(ch.lower(), 0) + 1
                min_len_word += 1
        
        res = None
        
        for w in words:
            if len(w) < min_len_word:
                continue
                
            d = dict()
            
            for ch in w:
                d[ch] = d.get(ch, 0) + 1
                
            if len(d.keys()) < len(store.keys()):
                continue
                
            for k in store:
                if d.get(k, 0) < store[k]:
                    break
            else:
                if res is None or len(w) < len(res):
                    res = w
            
        return res
    
"""
"1s3 PSt"
["step","steps","stripe","stepple"]
"1s3 456"
["looks","pest","stew","show"]
"Ah71752"
["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]
"""