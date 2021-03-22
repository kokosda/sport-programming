class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) is 1:
            return 0
        
        s1 = 0
        s2 = sum(nums)
        res = 0
        
        while res < len(nums):
            s2 -= nums[res]
            
            if s1 == s2:
                return res
                
            s1 += nums[res]
            res += 1
            
        return -1

"""
[-2,2]
s1: 0 -> -2 -> 0
s2: 0 -> 2  -> 0 
res 0 -> 1  -> 2

[-2,2]
[-2,0]
[0]
[-1,-1,-1,-1,-1,2]
[-1,-1,-1,-1,-1,0]
[2,1,-1]
[1,1]
[2,5]
[4,1,7,3,1,5,6]
[0,1,7,3,1,5,6]
[1,7,2,1,5,6]
[1,7,3,6,5,6]
"""