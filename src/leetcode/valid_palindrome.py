class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        it1, it2 = 0, len(s) - 1
        range1 = [ord('0'), ord('9')]
        range2 = [ord('a'), ord('z')]
        s = s.lower()
        
        def is_in_range(char: str) -> bool:
            ord_char = ord(char)            
            res = (ord_char >= range1[0] and ord_char <= range1[1]) or (ord_char >= range2[0] and ord_char <= range2[1])
            return res
        
        str1, str2 = '', ''
        len_s = len(s)
        
        while it1 < it2:
            while it1 < len_s and not is_in_range(s[it1]):
                it1 += 1
                
            while it2 >= 0 and not is_in_range(s[it2]):
                it2 -= 1
                
            if it1 == len_s or it2 < 0:
                break
                
            if s[it1] != s[it2]:
                return False
            else:
                str1 += s[it1]
                str2 += s[it2]
                it1 += 1
                it2 -= 1
                
        res = str1 == str2
        return res
