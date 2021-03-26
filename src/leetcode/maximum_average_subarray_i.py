class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums)
        
        i, j = 0, k - 1
        res = sum(nums[i:j + 1])
        tmp_sum = res
        pi = i
        i += 1
        j += 1
        
        while j < len(nums):
            tmp_sum = tmp_sum - nums[pi] + nums[j]
            res = max(res, tmp_sum)
            pi = i
            i += 1
            j += 1
        
        res /= k
        return res
    
"""
[1,12,-5,-6,50,3]
4
[8,0,1,7,8,6,5,5,6,7]
5
[9,7,3,5,6,2,0,8,1,9]
6
[0,1,1,3,3]
4
[7,4,5,8,8,3,9,8,7,6]
7
[90,40,-3,5,2,5,-100,4500]
1
[90,40,-3,5,2,5,-100,4500]
2
[1,12,-5,-6,50,3]
4
[14,7,-40,-300,90,2]
4
"""