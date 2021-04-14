class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = sorted(nums, key=lambda x: abs(x))
        return [num ** 2 for num in res]
    
    def sortedSquares_cache(self, nums: List[int]) -> List[int]:
        cache = [0] * (10 ** 4 + 1)
        
        for i in range(len(nums)):
            cache[abs(nums[i])] += 1
            
        res = []
        
        for i in range(len(cache)):
            while cache[i] > 0:
                res.append(i ** 2)
                cache[i] -= 1
                
        return res