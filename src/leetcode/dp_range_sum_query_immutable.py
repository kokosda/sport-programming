class NumArray:

    def __init__(self, nums: List[int]):
        self.__nums__ = nums
        self.__dp__ = [0] * (len(nums) + 1)
        self.__precalc__()

    def sumRange(self, i: int, j: int) -> int:
        res = self.__dp__[j + 1] - self.__dp__[i]
        return res
        
    def __precalc__(self):
        nums = self.__nums__
        dp = self.__dp__
        
        for i, _ in enumerate(nums):
            dp[i + 1] = dp[i] + nums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

"""
["NumArray","sumRange","sumRange","sumRange","sumRange"]
[[[2,5,1,-1,4,6,1,3]],[2,4],[3,5],[0,5],[1,1]]
["NumArray","sumRange","sumRange","sumRange","sumRange"]
[[[2,5,0,-1,4,6,1,3]],[2,4],[3,5],[0,5],[1,1]]
["NumArray","sumRange","sumRange","sumRange"]
[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]
["NumArray"]
[[[]]]
["NumArray","sumRange"]
[[[1]],[0,0]]
["NumArray","sumRange"]
[[[2,5]],[0,0]]
"""