class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hm = dict()
        
        for i in deck:
            hm[i] = hm.get(i, 0) + 1
            
        min_group = 2 ** 31 - 1
        
        for k in hm:
            min_group = min(min_group, hm[k])
        
        if min_group < 2:
            return False
        
        for k in hm:
            if hm[k] == min_group:
                continue
                
            if hm[k] < 2:
                return False
                
            if hm[k] % min_group is not 0:
                min_group = self._get_gcd(hm[k], min_group)
                
                if min_group < 2:
                    return False
            
        return True
    
    def _get_gcd(self, x: int, y: int) -> int:
        while y:
            x = x % y
            t = x
            x = y
            y = t
            
        return x
    
"""
[1,2,3,4,4,3,2,1]
[1,1,1,2,2,2,3,3]
[1]
[1,1]
[1,1,2,2,2,2]
[1,1,1,1,2,2,2,2,2,2]

18 | 14
18 % 14 = 1(4)
14 % 4 = 
"""