class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        dp1 = [0] * (len(nums) - 1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])
        
        dp2 = [0] * len(nums)
        dp2[0] = 0
        dp2[1] = nums[1]
        
        for i in range(2, len(nums)):
            dp2[i] = max(dp2[i-2] + nums[i], dp2[i-1])
            
        print(dp1, dp2)
        res = max(dp1[-1], dp2[-1])        
        return res

"""
state: money
value func: maximize sum without alerting the police
initial state: dp[0]
transition funcs:
    1) 1 house: return nums[0]
    2) 2 houses: return 0
    3) 3 houses: max(nums)
    4) >3 houses: dp[i] = max(dp[i-1] + nums[i+1])
order:
answer:

input: [8,0,1,2,5,3]
[8,1,5]
[8,1,3] - impossible
[8,2,3]
[0,2,8] - impossible
[0,5,8] - impossible
[1,5,8]
[2,3,8]
[5,8,1]

[4] - return 4 (4)
[4,5] - return 0 (5)
[4,5,1] - return 5 (5)
[4,5,1,2,(4)] - return 7 (4 or 5 or 1 or 2 or 4+1 or 4+2 or 5+2)

[4,1,1,9,5,(4)]
4:
    i+2
    i+3
1:
    i+2
    i+3
1:
    i+2
    i+3 - out of bound
9:
    i+2 - out of bound
    i+3 - out of bound
5:
    i+2 - out of bound
    i+3 - out of bound
    
if n > 3 then pre-last can be added to the 1st

input: [4,1,3,9,15,1,2,(4)]
dp: [4,1,4+3,9+4,15+(4+3),0]
dp: [4,4,7,13,22,22]

input: [1,4,1,3,9,15,1,2,(4)]
dp: [1,4,4,7,0,0,0]

dp[i] = max(nums[i] + dp[i-2], dp[i-1])

tests:
[4,1,1,9,5]
[8,0,1,2,5,3]
[2,3,2]
[4]
[4,5]
[4,5,1]
[4,5,1,2]

"""