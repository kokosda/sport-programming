class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums) - 1
        
        while i >= 2:
            p = (nums[i] + nums[i - 1] + nums[i - 2]) / 2
            sub_res = p * (p - nums[i]) * (p - nums[i - 1]) * (p - nums[i - 2])
            
            area = 0
            
            if sub_res > 0:
                area = sqrt(sub_res)
            
            if area > 0:
                return nums[i] + nums[i - 1] + nums[i - 2]
            
            i -= 1
        
        return 0
        
"""
[4,6,1,5,8,15,7]
[1,4,5,6,7,8,15]
"""