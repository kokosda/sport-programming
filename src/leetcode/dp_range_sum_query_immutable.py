class NumArray:

    def __init__(self, nums: List[int]):
        self.__nums__ = nums
        self.__dp__ = [[0] * len(nums) for _ in range(len(nums))]
        self.__precalculate_sums()

    def sumRange(self, i: int, j: int) -> int:
        res = self.__dp__[i][j]
        return res
    
    def __precalculate_sums(self):
        dp = self.__dp__
        nums = self.__nums__
        
        for i in range(len(nums)):
            dp[i][i] = nums[i]
            
            for j in range(i + 1, len(nums)):
                dp[i][j] = nums[j] + dp[i][j - 1]
                
        #for dpi in dp:
         #   print(*dpi)
        #print()

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

"""
input: [2,5,0,-1,4,6,1,3]
dp: [2, 7, 7, 6]
(2;4): 0 + -1 + 4 = 3
(3;5): -1 + 4 + 6 = 9

"""