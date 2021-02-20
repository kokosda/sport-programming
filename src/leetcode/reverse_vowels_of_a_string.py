class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        vowels = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' }
        list_s = list(s)
        
        i, j = 0, len(s) - 1
        i_v, j_v = False, False
        
        while i < j:
            if i_v == False:
                if s[i] not in vowels:
                    i += 1
                else:
                    i_v = True
                
            if j_v == False:
                if s[j] not in vowels:
                    j -= 1
                else:
                    j_v = True
                
            if i_v and j_v:
                list_s[i], list_s[j] = list_s[j], list_s[i]
                i_v, j_v = False, False
                i += 1
                j -= 1
                
        res = "".join(list_s) 
        return res