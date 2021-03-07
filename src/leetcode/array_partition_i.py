class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        SHIFT = 10 ** 4
        store = [0] * (2 * SHIFT + 1)
        
        for num in nums:
            store[SHIFT + num] += 1
               
        switched = False
        res = 0
        
        for i in range(len(store)):
            while store[i] > 0:
                if switched:
                    store[i] -= 1
                    switched = False
                    continue
                    
                if store[i] == 1:
                    store[i] -= 1
                    res += i - SHIFT
                    switched = True
                else:
                    store[i] -= 2
                    res += i - SHIFT

        return res
    
    def arrayPairSum_sort(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        
        for i in range(0, len(nums), 2):
            res += min(nums[i], nums[i + 1])
            
        return res
    
"""
[6214, -2290, 2833, -7908]
[1,4,3,2]
[6,2,6,5,1,2]
"""