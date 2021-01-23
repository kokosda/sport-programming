class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        INF = 10 ** 5
        dp = [INF] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > dp[i - 1]:
                dp[i] = nums[i]
            else:
                left_index = bisect.bisect_left(dp, nums[i], 0, i)
                dp[left_index] = nums[i]
        
        res = bisect.bisect_left(dp, INF)
        return res
    
"""
[0,3,1,6,2,2,7]
[
    0
    3
    1
    6
    2
    2
    7
]

[0,8,1,0,7]
[0] - 1

[0,8] - 2
[0,8,1] - 2
[0,8,1,0] - 2
[0,8,1,0,7] - 2

[0,1] - 2
[0,8,1,0] - 2
[0,8,1,0,7] - 3

[0,3,1,6,9,2,2,7,10]
[(0, 0), (1, 2), (2, 4), (2, 5), (3, 1), (6, 3), (7, 6)] - O(n^2) solution
0,1,6,9
0,1,2,9
0,1,2,7,10

[0,3,1,6,9,2,2,3,4,5,7,10]
0,1,6,9
0,1,2,9
0,1,2,3
0,1,2,3,4,5,7,10

[0,3,1,6,9,10,2,2,3,4,5,7,10]
0,1,2,3,4

[3,0,2]
[3]
[0,3,1]
[0,3,]
"""
