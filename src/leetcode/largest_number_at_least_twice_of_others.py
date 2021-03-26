class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) is 1:
            return 0
        
        prev_m = min(nums[0], nums[1])
        m = max(nums[0], nums[1])
        m_i = 0 if nums[0] > nums[1] else 1
        
        for i in range(2, len(nums)):
            if nums[i] >= m:
                prev_m = m
                m_i = i
                m = nums[i]
            elif nums[i] > prev_m:
                prev_m = nums[i]
                
        return m_i if prev_m * 2 <= m else -1