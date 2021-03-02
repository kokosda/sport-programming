class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        self.CAP_A = ord('A')
        self.CAP_Z = ord('Z')
        
        if self._is_all_caps(word):
            return True
        
        if self._is_all_low(word):
            return True
        
        if self._is_first_cap(word):
            return True
        
        return False
        
    def _is_all_caps(self, word: str) -> bool:
        for i in range(len(word)):
            if self.CAP_A <= ord(word[i]) <= self.CAP_Z:
                continue
            else:
                return False
        
        return True
    
    def _is_all_low(self, word: str) -> bool:
        LOW_A = ord('a')
        LOW_Z = ord('z')
        
        for i in range(len(word)):
            if LOW_A <= ord(word[i]) <= LOW_Z:
                continue
            else:
                return False
        
        return True
    
    def _is_first_cap(self, word: str) -> bool:
        if word[0].isupper() == False:
            return False
        
        if len(word) > 1:
            return self._is_all_low(word[1:])
        else:
            return True