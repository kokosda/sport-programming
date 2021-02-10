class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = nums[0], 1
        
        for i in range(1, len(nums)):
            if major == nums[i]:
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    major = nums[i]
                    
        return major
    
"""
[2,1,3,1,1,2,2,2,2]
m1: 2
m2: 1
c1: 2
c2: 3
"""