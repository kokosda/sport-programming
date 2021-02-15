class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        
        res = []
        counter = 1
        res.append(str(nums[0]))
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                counter += 1
            else:
                if counter > 1:
                    res[-1] += '->' + str(nums[i - 1])

                res.append(str(nums[i]))
                counter = 1
                
        if counter > 1:
            res[-1] += '->' + str(nums[-1])
                
        return res
                
"""
-49 4 843 3994 4888 4889 4890
"""