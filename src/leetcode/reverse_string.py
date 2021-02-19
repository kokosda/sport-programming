class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) < 2:
            return
        
        i = 0
        j = len(s) - 1
        
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            
"""
["h","e","l","l","o"]
["h","e","l","l","H"]
["h","e","l","l","o","w"]
[]
["f"]
"""