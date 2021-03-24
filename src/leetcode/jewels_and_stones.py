class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        res = 0
        
        for stone in stones:
            if stone in j:
                res += 1
                
        return res