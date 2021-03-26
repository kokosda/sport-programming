class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res, cur = 0, 1
        prev_num = nums[0]
        
        for i in range(1, len(nums)):
            if prev_num < nums[i]:
                cur += 1
            else:
                res = max(res, cur)
                cur = 1
                
            prev_num = nums[i]
        else:
            res = max(res, cur)
                
        return res