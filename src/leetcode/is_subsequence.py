class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        last_k = -1
        
        for k in s:
            k_was_found = False
            
            for i in range(last_k + 1, len(t)):
                if t[i] == k:
                    last_k = i
                    k_was_found = True
                    break
                    
            if not k_was_found:
                return False
            
        return True