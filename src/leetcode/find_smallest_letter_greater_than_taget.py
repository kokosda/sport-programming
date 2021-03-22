class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        store = [0] * 26
        a_code = ord('a')
        unique = set(letters)
        
        for ch in unique:
            store[ord(ch) - a_code] = 1
        
        t_code = ord(target) - a_code
        
        for i in range(len(store)):
            if i > t_code and store[i] is 1:
                return chr(i + a_code)
        
        return chr(store.index(1) + a_code)