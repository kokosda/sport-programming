class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        dp_plus = [0] * (len(nums) + 1)
        dp_minus = [0] * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            p_plus = max(nums[i-1], nums[i-1] * dp_plus[i - 1], nums[i-1] * dp_minus[i - 1])
            p_minus = min(nums[i-1], nums[i-1] * dp_minus[i - 1], nums[i-1] * dp_plus[i - 1])
            
            if p_plus > 0:
                dp_plus[i] = p_plus
            else:
                dp_minus[i] = p_plus
                
            if p_minus > 0:
                dp_plus[i] = p_minus
            else:
                dp_minus[i] = p_minus
        
        res = max(dp_plus)
        return res
    
"""
input: [2,3,-2,4]

state: contigious subarray [i,j]
value func: largest product dp[n][n]
initial: dp[0] = nums[0]
transition: dp[i] = max(nums[i], nums[i] * dp[i - 1])
order: 1..n, i..n
answer: dp[n]

[-5,10,15,-20]

[2,-5,3,-2]
dp+[0, 2, 0,  3,  60]
dp-[0, 0,-10,-30, -6]

[-2,5,-3,2,-1]
dp+[0, 0, 5,  30,  60,30]
dp-[0, -2,-10,-15, -30,-60]

-p = nums[i] * dp-[i-1]
+p = nums[i] * dp+[i-1]

if +p > 0:
    dp+[i] = +p
else:
    dp-[i] = +p
    
if -p < 0:
    dp-[i] = -p
else:
    dp+[i] = -p
    
[-2,3,-4]
[2,3,-2,4]
[2,3,-2,4,1,0,18,20,1,5,1,4,4,1,3,-2,0,-17,13,100]
[-2,0,-1]
[]
[1]
[4,4,4,4]
[-2]
"""