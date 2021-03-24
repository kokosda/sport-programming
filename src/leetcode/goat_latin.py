class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = set('aeiouAEIOU')
        caps = set(string.ascii_uppercase)
        res = []
        split = S.split(' ')
        
        for i in range(len(split)):
            w = split[i]
            
            if w[0] in vowels:
                res.append(f'{w}ma{"a" * (i + 1)}')
            else:
                res.append(f'{w[1:]}{w[0]}ma{"a" * (i + 1)}')
        
        return ' '.join(res)