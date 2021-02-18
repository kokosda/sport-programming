class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        n = len(nums)
        
        for i in nums:
            s += i
            
        sa = ((n + 1) * n) // 2
        
        return sa - s
"""
[8,6,4,2,3,5,7,0,1]
[0,0,0,0,0,0,0,0,0]
"""