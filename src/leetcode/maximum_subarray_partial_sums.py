class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        precalcedSums = self.__precalc(nums)
        max_sum = 0
        for i in enumerate(precalcedSums):
            max_sum += max(max_sum, self.__get(0, i, precalcedSums))
            
        print(precalcedSums)
        return max_sum
    
    def __precalc(self, a: List[int]) -> List[int]:
        res = [0] * (len(a) + 1)
        
        for i in range(len(a)):
            res[i + 1] = res[i] + a[i]
        
        return res
            
    def __get(self, l, r, a):
        if r + 1 == len(a):
            return 0
        return a[r + 1] - a[l]