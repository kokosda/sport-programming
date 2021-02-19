class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zc = 0
        
        while i < len(nums):
            if nums[i] == 0:
                zc += 1
            elif zc > 0:
                nums[i - zc] = nums[i]
                nums[i] = 0
                
            i += 1
        return nums
        
        
"""
[0,0,1,4,0,3,12]
[1,0,0,4,0,3,12]
[1,4,0,0,0,3,12]
i=0
"""