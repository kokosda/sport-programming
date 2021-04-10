class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        res = list(S)
        i = 0
        j = len(res) - 1
        
        while i < j:
            while i < j and res[i].isalpha() is False:
                i += 1
                
            while i < j and res[j].isalpha() is False:
                j -= 1
                
            tmp = res[i]
            res[i] = res[j]
            res[j] = tmp
            
            i += 1
            j -= 1
            
        return ''.join(res)