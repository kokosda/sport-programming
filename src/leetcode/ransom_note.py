class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = dict()
        
        for ch in magazine:
            if letters.get(ch):
                letters[ch] += 1
            else:
                letters[ch] = 1
            
        for ch in ransomNote:
            if letters.get(ch) and letters[ch] > 0:
                letters[ch] -= 1
            else:
                return False
            
        return True
    
    def canConstruct_list(self, ransomNote: str, magazine: str) -> bool:
        letters = [0] * 26
        ENCODING_SHIFT = 97
        
        for ch in magazine:
            letters[ord(ch) - ENCODING_SHIFT] += 1
            
        for ch in ransomNote:
            diff = ord(ch) - ENCODING_SHIFT
            letters[diff] -= 1
                
            if letters[diff] < 0:
                return False
            
        return True
    
"""
"a"
"b"
"aa"
"ab"
"aa"
"aab"
"""