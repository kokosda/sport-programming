class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        d1 = self._get_stat(A.split())
        d2 = self._get_stat(B.split())
        res = []
        
        for k in d1:
            if d1[k] is 1 and d2.get(k) is None:
                res.append(k)
                
        for k in d2:
            if d2[k] is 1 and d1.get(k) is None:
                res.append(k)
                
        return res                

    def _get_stat(self, words: List[str]) -> Dict[str, int]:
        res = dict()
        
        for w in words:
            res[w] = res.get(w, 0) + 1
            
        return res