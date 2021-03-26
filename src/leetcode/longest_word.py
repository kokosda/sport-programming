class Solution:
    def longestWord(self, words: List[str]) -> str:
        hs = set(words)        
        words.sort(reverse=True)
        matches = []
        max_len = 0
        
        for w in words:
            for i in range(1, len(w)):
                if w[:i] not in hs:
                    break                 
            else:
                if len(w) >= max_len:
                    matches.append(w)
                    max_len = len(w)
                    
        res = None
            
        for w in matches:
            if len(w) == max_len:
                res = w
                
        return res
    
"""
["b","br","bre","brea","break","breakf","breakfa","breakfas","breakfast","l","lu","lun","lunc","lunch","d","di","din","dinn","dinne","dinner"]
["w","wo","wor","worl","world"]
["a", "banana", "app", "appl", "ap", "apply", "apple"]
"""