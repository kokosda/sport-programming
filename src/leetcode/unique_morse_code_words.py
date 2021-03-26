class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        a_code = ord('a')
        res = set()
        
        for w in words:
            trans = ''.join(table[ord(ch) - a_code] for ch in w)
            res.add(trans)
            
        return len(res)