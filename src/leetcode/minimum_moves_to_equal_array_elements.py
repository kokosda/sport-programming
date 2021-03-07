class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_el = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < min_el:
                min_el = nums[i]
                
        res = 0
        
        for i, v in enumerate(nums):
            if v != min_el:
                res += v - min_el
                
        return res
    
"""
[0,2,3] => [1,3,3] => [2,4,3] => [3,5,3] => [4,5,4] => [5,5,5]
                      [2,4,3] => [3,4,4] => [4,5,5] => [5,6,5]
                      
[0,2,4,3] => [1,3,4,4] => [2,4,5,4] => [3,5,6,4] => [4,6,7,4] => [5,7,7,5] => [6,8,7,6] => [7,8,8,7] => [8,8,9,8] => [9,9,9,9]

[1,2,5,4]

"""