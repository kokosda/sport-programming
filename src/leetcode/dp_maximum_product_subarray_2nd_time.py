class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp_pos = [0] * (len(nums) + 1)
        dp_neg = [0] * (len(nums) + 1)
        max_pos = nums[0]
        
        for i in range(len(nums)):
            dp_pos[i] = max(dp_pos[i - 1] * nums[i], dp_neg[i - 1] * nums[i], nums[i])
            dp_neg[i] = min(dp_pos[i - 1] * nums[i], dp_neg[i - 1] * nums[i], nums[i])
            
            max_pos = max(max_pos, dp_pos[i])
            
        return max_pos

"""
input: [-1,4,-1,0,2,3,-3,-2]
dp+: [0, 0, 4, 4,0,2,6,0,36]
dp-: [0,-1,-4,-4,0,0,0,-18,0]

input: [-1,4,-2,5,2,3,-3,-2]
dp+: [0, 0, 4, 8, 40, 80, 240, 720, 1440]
dp-: [0,-1,-4,-8,-40,-80,-240,-720,-1440]

input: [0,4,-2,  5,  2,   3, -3,   -2]
dp+: [0,0,4, 0,  5, 10,  30,720,  180]
dp-: [0,0,0,-8,-40,-80,-240,-90,-1440]

input: [2,3,-2,4]
dp+: [0,2,4, 0,  5, 10,  30,720,  180]
dp-: [0,0,0,-8,-40,-80,-240,-90,-1440]
"""