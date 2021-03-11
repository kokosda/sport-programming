class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = set(candyType)
        MAX_CANDIES = len(candyType) // 2
        
        if len(types) <= MAX_CANDIES:
            return len(types)
        
        return MAX_CANDIES