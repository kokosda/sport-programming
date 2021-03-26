class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        res = True
        
        while i < j:
            if s[i] != s[j]:                
                if i + 1 < j:
                    res = self._is_palindrome(s, i + 1, j)
                if i < j - 1:
                    res = res or self._is_palindrome(s, i, j - 1)
                    
                return res
                
            i += 1
            j -= 1
            
        return res
            
    def _is_palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
                
            i += 1
            j -= 1
            
        return True
            
            
"""
aabcccccbcaa
  ^      ^
"""