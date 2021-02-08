from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0        
        if len(haystack) < len(needle):
            return -1
        
        prefixes = self.__get_prefixes__(needle)
        
        k, l = 0, 0
        
        while k < len(haystack):
            if haystack[k] == needle[l]:
                k += 1
                l += 1
                
                if l == len(needle):
                    return k - l
            elif l == 0:
                k += 1
            else:
                l = prefixes[l - 1]
            
        return -1
    
    def __get_prefixes__(self, needle: str) -> List[int]:
        res = [0] * len(needle)
        
        i, j = 1, 0
        
        while i < len(needle):
            if needle[i] == needle[j]:
                res[i] = j + 1
                i += 1
                j += 1
            elif j == 0:
                res[i] = 0
                i += 1
            else:
                j = res[j - 1]
                
        return res
    
"""
aabaaab
"abcabeabcabcabd"
"abcabd"

"""

s = Solution()
s.strStr('abcabeabcabcabd', 'abcabd')