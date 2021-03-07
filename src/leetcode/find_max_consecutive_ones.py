class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons_ones, cur_max_ones = 0, 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                cur_max_ones += 1
            else:
                max_cons_ones = max(max_cons_ones, cur_max_ones)
                cur_max_ones = 0
        else:
            max_cons_ones = max(max_cons_ones, cur_max_ones)
                
        return max_cons_ones