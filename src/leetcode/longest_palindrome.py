class Solution:
    def longestPalindrome(self, s: str) -> int:
        ALPHABET_LEN = 26
        letters = [0] * 2 * ALPHABET_LEN
        A_CAP = ord('A') - ALPHABET_LEN
        A_LOW = ord('a')
        Z_LOW = ord('z')
        
        for ch in s:
            if A_LOW <= ord(ch) <= Z_LOW:
                letters[ord(ch) - A_LOW] += 1
            else:
                letters[ord(ch) - A_CAP] += 1
            
        res = 0
        can_add_one = False
        
        for count in letters:
            if count > 1:
                res += count if count % 2 == 0 else count - 1
            elif count == 1:
                can_add_one = True
                
        if can_add_one == False:            
            for i in letters:
                if i % 2 != 0:
                    can_add_one = True
                    break
                
        if can_add_one:
            res += 1
            
        return res
    
"""
"abccccdd"
"a"
"aaa"
"aca"
"zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez"
"""