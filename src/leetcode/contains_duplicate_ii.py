class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        values = dict()
        
        for i in range(len(nums)):
            if nums[i] not in values:
                values[nums[i]] = i
            else:
                if i - values[nums[i]] <= k:
                    return True
                else:
                    values[nums[i]] = i
        
        return False

    
"""
[1,1,1,1,1,1,1], k = 5

"""